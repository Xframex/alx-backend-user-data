#!/usr/bin/env python3
'''session_exp_auth'''

from flask import request
from datetime import datetime, timedelta


from .session_auth import SessionAuth

class SessionExpAuth(SessionAuth):
    '''SessionExpAuth'''

    def __init__(self):
        '''constructor'''
        super().__init__()
        self.session_duration = 0

    def create_session(self, user_id=None):
        '''create_session'''
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {
                'user_id': user_id,
                'created_at': datetime.now()
            }
            return session_id
        return None

    def valid_session(self, session_id):
        '''valid_session'''
        if session_id in self.user_id_by_session_id:
            if self.session_duration <= 0:
                return True
            created_at = self.user_id_by_session_id[session_id]['created_at']
            if (created_at + timedelta(seconds=self.session_duration) <
                    datetime.now()):
                return False
            return True
        return False

    def destroy_session(self, request=None):
        '''destroy_session'''
        if request:
            session_id = self.session_cookie(request)
            if session_id:
                if session_id in self.user_id_by_session_id:
                    del self.user_id_by_session_id[session_id]
                    return True
        return False

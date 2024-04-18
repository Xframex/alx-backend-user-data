#!/usr/bin/env python3
"""Session authentication module for the API.
"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session authentication class.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id.
        """
        if user_id is None or type(user_id) != str:
            return None
        user_id = str(uuid.uuid4())
        self.user_id_by_session_id[user_id] = user_id
        return user_id

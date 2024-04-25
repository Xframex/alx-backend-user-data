#!/usr/bin/env python3
'''auth module'''
from base64 import b64encode


def _hash_password(password: str) -> bytes:
    '''hashes a password'''
    return b64encode(password.encode()).decode()

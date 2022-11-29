import os
import secrets

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex()
    DEBUG = False
    TESTING = False

import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = 'CLAVE SECRETA'
    SESSION_COOKIE_SECURE = False
    
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Logd031211@127.0.0.1:3306/bdidgs802'
    """ SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 300,
    }
    SQLALCHEMY_SESSION_OPTIONS = {
        "expire_on_commit": False,
    }
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_NAME = "session"
    SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_PATH = None
    SESSION_REFRESH_EACH_REQUEST = True
    SESSION_PERMANENT = True
    SESSION_USE_SIGNER = True
    SESSION_TYPE = "sqlalchemy"
    SESSION_SQLALCHEMY_TABLE = "sessions"
    SESSION_SQLALCHEMY = create_engine(SQLALCHEMY_DATABASE_URI)
    SESSION_SQLALCHEMY_SESSION = sessionmaker(bind=SESSION_SQLALCHEMY)
    SESSION_SQLALCHEMY_CREATE_SCHEMAS = True """
import os

class Config(object):
    DEBUG=False
    SECRET_KEY = 'SUPRESECRETKEY'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost:5432/jim'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')

    WTF_CSRF_ENABLE = True

    #Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 15
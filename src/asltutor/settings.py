import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    ENV = 'development'
    SECRET_KEY = b'N\x11r\xd6\xb4\x07\x9b\xe7\xcbY)\x80n\xf0e\xfd'
    MONGODB_SETTINGS = {
        'db': 'asl',
        'host': 'mongodb://localhost:27017/asl_tutor'
    }


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGODB_SETTINGS = {
        'db': 'asl',
        'host': 'mongodb://localhost:27017/asl_tutor'
    }
    S3_BUCKET = os.environ.get("S3_BUCKET")
    S3_KEY = os.environ.get("S3_KEY")
    S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

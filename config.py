import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/expense'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace(".//", "ql://", 1)


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/expense'
    SECRET_KEY = 'jibberishjibberish'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jidraph:6720@localhost/expense'
    SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    pass


class DevConfig(Config):

    SECRET_KEY = 'jibberishjibberish'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
import os


# CREATE DATABASE livro_flask CHARACTER SET UTF8 collate utf8_general_ci

class Config:
    CSRF_ENABLE = True  # Habilita o uso de criptografia no flask
    SECRET = 'AOPYU76%#AS'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None  # Receberá as propriedades do app

    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://user:passwd@host:port/databae'


class DevelopmentConfig(Config):
    TESTING = True  # Warning e error ficam habilitados
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 5000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/'


app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()

}

app_active = os.getenv('FLASH_ENV')

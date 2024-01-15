from flask_mail import Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = 'bbar67441@gmail.com '
MAIL_PASSWORD = 'mxpu ayas sjwk kuaj'

class Config (object):
    MAIL_SERVER = MAIL_SERVER
    MAIL_PORT = MAIL_PORT
    MAIL_USE_SSL = MAIL_USE_SSL
    MAIL_USE_TLS = MAIL_USE_TLS
    MAIL_USERNAME = MAIL_USERNAME
    MAIL_PASSWORD = MAIL_PASSWORD

    SECRET_KEY = 'my_secret_key123456'
    DATABASE_URI = 'sqlite:///app/database/bluebullbar.db'

class DevelopmentMode(Config):
    DEBUG=True
    

class ProductionMode(Config):
    DEBUG=False

mail=Mail()
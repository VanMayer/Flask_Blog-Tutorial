import os


class Config:
    SECRET_KEY = '125946380086878817f1f47a2d86b81b'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email_user')
    MAIL_PASSWORD = os.environ.get('email_pass')
    MONGODB_SETTINGS = {
        'username': os.environ.get("MONGODB_BLOG_USERNAME"),
        'password': os.environ.get("MONGODB_BLOG_PASSWORD"),
        'host': os.environ.get("MONGODB_DATABASE_BLOG_URI")
    }

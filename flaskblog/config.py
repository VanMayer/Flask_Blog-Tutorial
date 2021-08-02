import os
import ssl


class Config:
    SECRET_KEY = '125946380086878817f1f47a2d86b81b'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('email_user')
    MAIL_PASSWORD = os.environ.get('email_pass')
    MONGODB_SETTINGS = {    
        'username': 'VanMay',
        'password': 'Blog2021ZO5',
        'host': 'mongodb+srv://flaskblog.ulelq.mongodb.net/PopCultureBlog'
    }

    #adding ?tlsAllowInvalidCertificates=true
    #mongodb+srv://<username>:<password>@<url for database server>/<database name>
    #mongodb+srv://flaskblog.ulelq.mongodb.net/mongoblog
    #mongodb+srv://flaskblog.ulelq.mongodb.net/myFirstDatabase
    #mongodb+srv://VanMay:<password>@flaskblog.ulelq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
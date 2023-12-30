import os


class Config(object):
    FLASK_APP = 'wsgi.py'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = 'MY_SECRET_KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///my_db.db'

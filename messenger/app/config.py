"""Configurations for 'Simple SMS Client'.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = ''
    DBUSER = ''
    DBHOST = ''
    DBPASS = ''
    DBNAME = ''

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    FB_ACCESS_TOKEN = os.environ.get('FB_ACCESS_TOKEN')
    FB_VERIFY_TOKEN = os.environ.get('FB_VERIFY_TOKEN')
    
    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = False
    HOST = '0.0.0.0'
    DBUSER = os.environ.get('DBUSER')
    DBHOST = '127.0.0.1'
    DBPASS = None
    DBNAME = 'cashbetdev'

    FB_ACCESS_TOKEN = os.environ.get('FB_ACCESS_TOKEN')
    FB_VERIFY_TOKEN = os.environ.get('FB_VERIFY_TOKEN')

class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'dev': Development,
    'prod': Production,

    'default': Development
}


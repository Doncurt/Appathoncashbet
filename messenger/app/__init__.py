# -*- encoding: utf-8 -*-

"""Main entrypoint into `Cashbet Chatbot` Flask and Postgres application."""

import os
from app.config import config
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from pymessenger.bot import Bot


"""CONFIG"""
app = Flask(__name__)

server_configuration = 'default'
app.config.from_object(config[server_configuration])
config[server_configuration].init_app(app)


"""DATABASE"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{user}:{dbpass}@{host}:5432/{db}'.format(
    user = app.config['DBUSER'],
    dbpass = app.config['DBPASS'],
    host = app.config['DBHOST'],
    db = app.config['DBNAME']
)


"""MESSENGER"""
bot = Bot(os.environ.get('FB_ACCESS_TOKEN'))


"""MESSAGING CLIENT"""
api = Api(app)

from app.client import MessengerClient
api.add_resource(MessengerClient, '/messenger')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jiayi Li'

import os

from flask import Flask, request, g, current_app
from pymongo import MongoClient
from app.filters import datetime_filter, markdown_filter

client = MongoClient()
db = client.test

from app.utilities import cookieToUser, cookieToView
from app.views.route import route
from app.views.api import api

def signInStatus():
    
    '''sign in status before each request'''
    
    cookie = request.cookies.get(current_app.config['COOKIE_NAME'], 'nothing')
    g.__user__ = cookieToUser(cookie)

def viewStatus():
    
    '''view mode status before each request'''
    
    cookie = request.cookies.get(current_app.config['COOKIE_NAME'], 'nothing')
    g.__view__ = cookieToView(cookie)
    
def create_app():
    
    '''create this application'''
    
    # create this flask app
    app = Flask(__name__)
    # configuration
    app.config.from_object('config.DevConfig')
    # add filters
    app.jinja_env.filters.update(datetime=datetime_filter, markdown=markdown_filter)
    # add before request functions
    app.before_request(signInStatus)
    app.before_request(viewStatus)
    # register routes
    app.register_blueprint(route)
    app.register_blueprint(api)
    return app
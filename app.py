#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:16:31 2018

@author: bibi
"""

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

# a resource represents something an api represents ...

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" # at the root folder of our project
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # turns off the flask sqlalchemy tracker but not the sqlalchemy tracker ... subtle
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # create new endpoint /auth

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db # in the if because of circular import
    db.init_app(app)
    app.run(port=5000, debug=True)


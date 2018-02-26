#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:23:49 2018

@author: bibi
"""

from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found"}, 404
    
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store '{}' already exist".format(name)}, 400 
        
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occured while creating the store"}, 500
        
        return store.json(), 201
    
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {"message": "Store deleted"}
    

class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
    
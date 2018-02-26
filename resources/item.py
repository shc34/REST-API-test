#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:59:23 2018

@author: bibi
"""
# CRUD API: Create, Read, Update, Delete

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser() # allows to select the information
    parser.add_argument('price',
        type = float,
        required = True, #be sure no request can come through with no price!
        help = "This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type = int,
        required = True, #be sure no request can come through with no price!
        help = "Every item needs a store id."
    )
    
    @jwt_required() #better to put it before all functions
    def get(self, name):
        
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': "Item not found"}, 404
        
    def post(self, name): #if called 10 times, 10 items, different from put where there will be only have one
        # first, deal with errors!
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists".format(name)}, 400 # 400: bad request, syntaxe requete erronee

        data = Item.parser.parse_args()        
        
        item = ItemModel(name, **data) # **data == data["price"], data["store_id"]
        
        try:
            item.save_to_db()
        except:
            return {"message": "An error occured inserting the item"}, 500 #500: internat server error
        
        return item.json(), 201 # requete traitee avec succes et creation du doc

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message": "Item deleted"}

        
    def put(self, name):
        
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data["price"]
            item.store_id = data["store_id"]
            
            
        item.save_to_db()
        
        return item.json()
    

class ItemList(Resource):
    
    def get(self):
        {"item": [item.json() for item in ItemModel.query.all()]}
        
# or even this is working with non pythoners        {"item": list(map(lambda x: x.json(), ItemModel.query.all()))}
        
        
        
        
        
        
        
        
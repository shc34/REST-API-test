#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:50:17 2018

@author: bibi
"""

import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    
    parser = reqparse.RequestParser() # allows to select the information
    parser.add_argument('username',
        type = str,
        required = True, #be sure no request can come through with no price!
        help = "This field cannot be left blank!"
    )
    parser.add_argument('password',
        type = str,
        required = True, #be sure no request can come through with no price!
        help = "This field cannot be left blank!"
    )
    
    def post(self):
                
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User with this username ( '{}' ) already exists".format(data['username'])}, 409
            
        user = UserModel(**data) # **data y a t il un ordre du coup?
        user.save_to_db()
        
        return {"message": "User created successfully"}, 201 # 201 = created
    
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




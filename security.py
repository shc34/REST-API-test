#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 15:42:58 2018

@author: bibi
"""

from werkzeug.security import safe_str_cmp
from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password): # better than == because safer with old versions beacause of encoding asky, utf8 ...
        return user
    
def identity(payload):
    user_id = payload["identity"]
    return UserModel.find_by_id(user_id)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
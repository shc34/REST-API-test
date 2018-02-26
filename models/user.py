#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 16:13:39 2018

@author: bibi
"""

from db import db


class UserModel(db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) # the size of the username is limited to 80 here
    password = db.Column(db.String(80))
    
    def __init__(self, username, password): #the id is done automatically
        self.username = username
        self.password = password
       
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def find_by_username(cls, username):        
        return cls.query.filter_by(username=username).first() 
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first() 
    

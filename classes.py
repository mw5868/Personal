# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:58:11 2018

@author: mwood
"""

class Dog:
    def _init_(self,name):
        self.name = name
        self.tricks = []
        
    def add_trick(self,trick):
        self.tricks.append(trick)

d = Dog("fido")

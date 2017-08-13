# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 10:52:56 2017

@author: Mark
"""

import math
import turtle

def drawCircle(x,y,r):
    turtle.up()
    turtle.setpos(x+r,y)
    turtle.down()
    
    for i in range(0,365,5):
        a = math.radians(i)
        turtle.setpos(x + r*math.cos(a),y + r*math.sin(a))
        
drawCircle(100,100,50)
turtle.mainloop()


class spiro:
    def _init_(self,xc,yc,col,R,r,l):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawingComplete = False
        self.setparams(xc,yc,col,R,r,l)
        self.restart()
        
def setparams(self,xc,yc,col,R,r,l):
    self.xc = xc
    self.yc = yc
    self.R = int(R)
    self.r = int(r)
    self.l = l
    self.col = col
    gcdVal = gcd(self.r,self.R)
    self.nRot = self.r//gcdVal
    self.k = r/float(R)
    self.t.color(*col)
    self.a=0

def restart(self):
    self.drawingComplete = False
    self.t.showturtle()
    self.t.up()
    R,k,l = self.R,self.k,self.l
    a = 0.0
    x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
    y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
    self.t.setpos(self.xc + x, self.yc + y)
    self.t.down()

def draw(self):
    R,k,l = self.R,self.k,self.l
    for i in range(0,365*self.nRot + 1, self.step):
        a = math.radians(i)
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc + x, self.yc + y)
    self.t.hideturtle()
    
    
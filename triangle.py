import pygame
import random

#設定色彩
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

class Triangle():
    def __init__(self,window,maxWidth,maxHeight):
        self.window=window
        self.width=random.randrange(10,100)
        self.height=random.randrange(10,100)
        self.triangleSlope=-1*(self.height/self.width)#斜率
        self.color=random.choice(RED,GREEN,BLUE)
        self.x=random.randrange(1,maxWidth-100)
        self.y=random.randrange(25,maxHeight-100)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.shapeType='triangle'

    def clickedInside(self,mousePoint):
        inRect=self.rect.collidepoint(mousePoint)
        if not inRect:
            return False
        #如果點在三角形中則進行一些運算
        xOffset=mousePoint[0]-self.x
        yOffset=mousePoint[0]-self.y
        if xOffset==0:
            return True
        pointSlopeFromYIntercept=(yOffset-self.height)/xOffset
        if pointSlopeFromYIntercept<self.triangleSlope:
            return True
        else:
            return False
    def getType(self):
        return self.shapeType
    def getArea(self):
        theArea=.5*self.width*self.height
        return theArea
    def draw(self):
        pygame.draw.rect(self.window,self.color,((self.x,self.y+self.height),(self.x,self.y),(self.x+self.width,self.y)))
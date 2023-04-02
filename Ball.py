import pygame
from pygame.locals import *
import random

class Ball():

    def __init__(self,window,windowWidth,windowHeight):
        self.window=window #記住視窗 等一下要繪製
        self.windowWidth=windowWidth
        self.windowHeight=windowHeight

        self.image=pygame.image.load('images/ball.png')
        #rect物件是由[x,y,width,height]產生
        ballRect=self.image.get_rect()
        self.widith=ballRect.width
        self.height=ballRect.height
        self.maxWidth=windowWidth-self.widith
        self.maxHeight=windowHeight-self.height

        #隨機挑選一個起始位置
        self.x=random.randrange(0,self.maxWidth)
        self.y=random.randrange(0,self.maxHeight)
        #速度也做成隨機
        speedsList=[-4,-3,-2,-1,1,2,3,4]
        self.xSpeed=random.choice(speedsList)
        self.ySpeed=random.choice(speedsList)

    def update(self):
        #檢測是否碰到邊界 如果有就反彈
        if(self.x<0) or (self.x>=self.maxWidth):
            self.xSpeed=-self.xSpeed
        
        if(self.y<0) or (self.y>=self.maxHeight):
            self.ySpeed=-self.ySpeed

        #更新球的座標
        self.x=self.x+self.xSpeed
        self.y=self.y+self.ySpeed
    
    def draw(self):
        self.window.blit(self.image,(self.x,self.y))

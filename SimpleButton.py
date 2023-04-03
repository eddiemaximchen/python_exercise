import pygame
from pygame.locals import *

class SimpleButton():
    #用來追蹤按鈕的狀態
    STATE_IDLE='idle'          #按鈕沒按住 游標不在按鈕上
    STATE_ARMED='armed'        #按鈕按下 游標在按鈕上
    STATE_DISARMED='disarmed'  #按鈕按下 但游標不在按鈕上

    def __init__(self,window,loc,up,down):
        self.window=window
        self.loc=loc
        self.surfaceUp=pygame.image.load(up)
        self.surfaceDown=pygame.image.load(down)

        #取得按鈕的物件 用來檢查游標是否在上面
        self.rect=self.surfaceUp.get_rect()
        self.rect[0]=loc[0]
        self.rect[1]=loc[1]

        self.state =SimpleButton.STATE_IDLE

    def handleEvent(self,eventObj):
        #如果滑鼠產生例外事件會回傳false
        if eventObj.type not in (MOUSEMOTION,MOUSEBUTTONUP,MOUSEBUTTONDOWN):
            return False
        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        #表示按鈕按下 游標在按鈕上
        if self.state == SimpleButton.STATE_IDLE:
            if(eventObj.type==MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state=SimpleButton.STATE_ARMED
        
        elif self.state==SimpleButton.STATE_ARMED:
            #按鈕按過 游標不在按鈕上
            if(eventObj.type==MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state=SimpleButton.STATE_IDLE
                return True
            
            if (eventObj.type==MOUSEMOTION) and (not eventPointInButtonRect):
                self.state=SimpleButton.STATE_DISARMED 
    
        elif self.state==SimpleButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state=SimpleButton.STATE_ARMED
            elif eventObj.type==MOUSEBUTTONUP:
                self.state=SimpleButton.STATE_IDLE

        return False

    def draw(self):
        #繪製按鈕目前的外觀到視窗中
        if self.state==SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown,self.loc)
        else:
            self.window.blit(self.surfaceUp,self.loc)
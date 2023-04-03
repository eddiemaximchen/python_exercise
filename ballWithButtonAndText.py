import pygame
from pygame.locals import *
from Ball import *
from SimpleButton import *
from SimpleText import *
import sys
import random

#定義常數
BLACK=(0,0,0)
WHITE=(255,255,255)
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
FRAMES_PER_SECOND=30

#初始化視窗
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()

#初始化變數
objBall=Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)
objFrameCountLabel=SimpleText(window,(60,20),'Program has run through this many loops: ',WHITE)
objFrameCountDisplay=SimpleText(window,(500,20),'',WHITE)
objRestartButton=SimpleButton(window,(280,60),'images/restartUp.png','images/restartDown.png')
frameCounter=0

#6持續執行的迴圈
while True:
    #7檢查和處裡事件
    for event in pygame.event.get():
        #8是否有點關閉按鈕 退出pygame和結束程式
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8每個影格要進行的動作
    if objRestartButton.handleEvent(event):
        frameCounter=0 #重新記數
    objBall.update()
    frameCounter=frameCounter+1
    objFrameCountDisplay.setValue(str(frameCounter))
    
    #9清除視窗
    window.fill(BLACK)

    #10繪製所有視窗元素
    objBall.draw()
    objFrameCountLabel.draw()
    objFrameCountDisplay.draw()
    objRestartButton.draw()
    #11更新視窗
    pygame.display.update()
    #12放慢速度
    clock.tick(FRAMES_PER_SECOND)


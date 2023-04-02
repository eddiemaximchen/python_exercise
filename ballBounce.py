import pygame
from pygame.locals import *
import sys
import random
from Ball import *

BLACK=(0,0,0)
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
FRAMES_PER_SECOND=30
#初始化視窗
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()
objBall=Ball(window,WINDOW_WIDTH,WINDOW_HEIGHT)
#4 載入相關內容 影像 聲音等
ballImage=pygame.image.load('images/ball.png')
bouncesound=pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1,0,0)
#6持續執行的迴圈
while True:
    #7檢查和處裡事件
    for event in pygame.event.get():
        #8是否有點關閉按鈕 退出pygame和結束程式
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8每個影格要進行的動作
    objBall.update()

    #9清除視窗
    window.fill(BLACK)

    #10繪製所有視窗元素
    objBall.draw()

    #11更新視窗
    pygame.display.update()
    #12放慢速度
    clock.tick(FRAMES_PER_SECOND)


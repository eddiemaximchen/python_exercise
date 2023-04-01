#pygame demo 只有視窗
import pygame
from pygame.locals import *
import sys
import random

BLACK=(0,0,0)
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
FRAMES_PER_SECOND=30
BALL_WIDTH_HEIGHT=100
MAX_WIDTH=WINDOW_WIDTH-BALL_WIDTH_HEIGHT
MAX_HEIGHT=WINDOW_HEIGHT-BALL_WIDTH_HEIGHT
TARGET_X=400
TARGET_Y=320
TARGET_WIDTH_HEIGHT=120
N_PIXELS_TO_MOVE=3

#初始化視窗
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()
#4 載入相關內容 影像 聲音等
ballImage=pygame.image.load('images/ball.png')
targetImage=pygame.image.load('images/target.jpg')
#5 初始化變數
ballX =random.randrange(MAX_WIDTH)
ballY=random.randrange(MAX_HEIGHT)
targetRect=pygame.Rect(TARGET_X,TARGET_Y,TARGET_WIDTH_HEIGHT,TARGET_WIDTH_HEIGHT)
#6持續執行的迴圈
while True:
    #7檢查和處裡事件
    for event in pygame.event.get():
        #8是否有點關閉按鈕 退出pygame和結束程式
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #看看使用者是否有按下按鍵
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                ballX=ballX-N_PIXELS_TO_MOVE
            elif event.key==pygame.K_RIGHT:
                ballX=ballX+N_PIXELS_TO_MOVE
            elif event.key==pygame.K_UP:
                ballY=ballY-N_PIXELS_TO_MOVE
            elif event.key==pygame.K_DOWN:
                ballY=ballY+N_PIXELS_TO_MOVE


    #8每個影格要進行的動作
    #檢測影像是否與目標有碰撞
    ballRect=pygame.Rect(ballX,ballY,BALL_WIDTH_HEIGHT,BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

    #9清除視窗
    window.fill(BLACK)
    #10繪製所有視窗元素
    #把球繪製在機的位置
    window.blit(targetImage,(TARGET_X,TARGET_Y)) #繪製target
    window.blit(ballImage,(ballX,ballY)) #繪製球
    #11更新視窗
    pygame.display.update()
    #12放慢速度
    clock.tick(FRAMES_PER_SECOND)

#pygame demo 只有視窗
import pygame
from pygame.locals import *
import sys
import random

BLACK=(0,0,0)
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
FRAMES_PER_SECOND=30
N_PIXELS_TO_MOVE=3

#初始化視窗
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock=pygame.time.Clock()
#4 載入相關內容 影像 聲音等
ballImage=pygame.image.load('images/ball.png')
#5 初始化變數 使用rect物件
ballRect = ballImage.get_rect()
MAX_WIDTH=WINDOW_WIDTH-ballRect.width
MAX_HEIGHT=WINDOW_HEIGHT-ballRect.height
ballRect.left=random.randrange(MAX_WIDTH)
ballRect.right=random.randrange(MAX_HEIGHT)
xSpeed=N_PIXELS_TO_MOVE
ySpeed=N_PIXELS_TO_MOVE

#6持續執行的迴圈
while True:
    #7檢查和處裡事件
    for event in pygame.event.get():
        #8是否有點關閉按鈕 退出pygame和結束程式
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #8每個影格要進行的動作
    if(ballRect.left<0)or (ballRect.right>=WINDOW_WIDTH):
        xSpeed=-xSpeed
    if (ballRect.top<0)or (ballRect.bottom>=WINDOW_HEIGHT):
        ySpeed=-ySpeed

    #更新球的位置
    ballRect.left=ballRect.left+xSpeed
    ballRect.top=ballRect.top+ySpeed
    #9清除視窗
    window.fill(BLACK)
    #10繪製所有視窗元素
    #把球繪製在隨機的位置
    window.blit(ballImage,ballRect)
    #11更新視窗
    pygame.display.update()
    #12放慢速度
    clock.tick(FRAMES_PER_SECOND)
import pygame
from pygame.locals import *
from SimpleButton import*
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

def mycallbackfunction():
    print('User pressed Button B, called mycallbackfunction')

class CallBackTest():
    def __init__(self):
        pass

    def myMethod(self):
        print('User pressed Button C, called myMethod of the CallBackTest object')

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

objCallBackTest=CallBackTest() #callback button
objButtonA =SimpleButton(window,(25,30),'images/buttonAUp.png','images/buttonADown.png')

#設定callback function
objButtonB=SimpleButton(window,(150,30),'images/buttonBUp.png','images/buttonBDown.png',callBack=mycallbackfunction)

#用物件設定callback function
objButtonC=SimpleButton(window,(275,30),'images/buttonCUp.png','images/buttonCDown.png',callBack=objCallBackTest.myMethod)

counter = 0

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if objButtonA.handleEvent(event):
        print('User pressed ButtonA,processed by if ')
    objButtonB.handleEvent(event)
    objButtonC.handleEvent(event)

    counter = counter +1

    window.fill(GRAY)
    objButtonA.draw()
    objButtonB.draw()
    objButtonC.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
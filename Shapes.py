import pygame
import sys
from pygame.locals import *
from square import *
from triangle import *
from circle import *
import pygwidgets

#設定常數
WHITE=(255,255,255)
WINDOW_WIDTH=640
WINDOW_HEIGHT=480
FRAMES_PER_SECOND=30
N_SHAPES=10

#設定視窗
pygame.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),0,32)
clock=pygame.time.Clock()

shapeList=[]
shapeClassesTuple=(Square,Circle,Triangle)
for i in range(0,N_SHAPES):
    randomlyChosenClass = random.choice(shapeClassesTuple)
    objShape=randomlyChosenClass(window,WINDOW_WIDTH,WINDOW_HEIGHT)
    shapeList.append(objShape)

objStatusLine = pygwidgets.DisplayText(window,(4,4),'Click on shapes',fontSize=28)

while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            #先檢查最後繪製的圖形
            for objShape in reversed(shapeList):
                if objShape.clickedInside(event.pos):
                    area=objShape.getArea()
                    area=str(area)
                    theType=objShape.getType()
                    newText=f'clicked on a {theType} whose area is {area}'
                    objStatusLine.setValue(newText)
                    break
    #繪製形狀
    window.fill(WHITE)
    for objShape in shapeList:
        objShape.draw()
    objStatusLine.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
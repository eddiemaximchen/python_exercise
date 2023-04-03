import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Define constants
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30 

# 2 - Initialize the window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
# Create an instance of SimpleButton
objButton1 = SimpleButton(window, (150, 0),
                        'images/buttonAUp.png',
                        'images/buttonADown.png')

objButton2 = SimpleButton(window, (150, 30),
                        'images/buttonBUp.png',
                        'images/buttonBDown.png')

objButton3 = SimpleButton(window, (150, 60),
                        'images/buttonCUp.png',
                        'images/buttonCDown.png')

# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pass the event to the button, see if it has been clicked on
        if objButton1.handleEvent(event):
            print('User has clicked buttonA.')

        if objButton2.handleEvent(event):
            print('User has clicked buttonB.')
    
        if objButton3.handleEvent(event):
            print('User has clicked buttonC.')

    # 8 - Do any "per frame" actions
    
    # 9 - Clear the window
    window.fill(GRAY)
    
    # 10 - Draw all window elements
    objButton1.draw() # draw the button
    objButton2.draw() # draw the button
    objButton3.draw() # draw the button
    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


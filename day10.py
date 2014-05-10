# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 16:29:18 2014

@author: sawyer
"""

import pygame, sys
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

windowSurfaceObject = pygame.display.set_mode((640,480))
pygame.display.set_caption("Sawyer's Game")

surfaceObj = pygame.image.load("sawyerArt.bmp")

redColor = pygame.Color(255,0,0)
blueColor = pygame.Color(0,255,0)
greenColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
mousex, mousey = 0,0

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello, World!'

soundObj = pygame.mixer.Sound("DropInTheOcean.mp3")

while True:
    windowSurfaceObject.fill(whiteColor)
    
    pygame.draw.polygon(windowSurfaceObject, greenColor, ((146,0), (291, 106), (236, 277), (56, 277), (0,106)))
    pygame.draw.circle(windowSurfaceObject, redColor, (300, 50), 20, 0)
    pygame.draw.ellipse(windowSurfaceObject, blueColor, (300, 250,40,80), 1)
    pygame.draw.rect(windowSurfaceObject, redColor, (10, 10, 50, 100))
    pygame.draw.line(windowSurfaceObject, blueColor, (60,160), (120,60), 4)
    
    pixArr = pygame.PixelArray(windowSurfaceObject)
    for x in range(100, 200, 4):
        for y in range(100, 200, 4):
            pixArr[x][y] = redColor
    del pixArr
    
    print windowSurfaceObject
    windowSurfaceObject.blit(surfaceObj, (mousex, mousey))
    
    msgSurfaceObj = fontObj.render(msg, False, blueColor)
    msgRectObj = msgSurfaceObj.get_rect()
    msgRectObj.topleft = (10,20)
    windowSurfaceObject.blit(msgSurfaceObj, msgRectObj)
    
    for event in pygame.event.get():
        if  event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            soundObj.play()
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            soundObj.play()
            if event.button in (1,2,3):
                msg = 'left, middle or right mouse click'
            elif event.button in (4,5):
                msg = 'mouse scrolled up or down'
        
        elif event.type == KEYDOWN:
            if event.key in (K_LEFT, K_RIGHT, K_DOWN, K_UP):
                msg = 'arrow key pressed'
            if event.key == K_a:
                msg = '"A" key pressed'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    pygame.display.update()
    fpsClock.tick(30)
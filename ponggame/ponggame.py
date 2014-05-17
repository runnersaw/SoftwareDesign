# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 16:12:57 2014

@author: sawyer
"""

import pygame, sys
from pygame.locals import *
from random import *
import math
import time

def game(users, player1Object, player2Object):
    
    size = (1000,500)
    paddleLength = 80
    maxVY = 10
    VX = 8
    goalLength = 300
    wallWidth = 10
    ballRadius = 10
    paddleV = 2
    winScore = 7
    
    class User:
        def __init__(self, name, win=0, loss=0):
            self.name = name
            self.win = win
            self.loss = loss
            
        def __str__(self):
            return self.name + str(self.win) + str(self.loss)
    
    class Ball:
        '''Encodes the information of a ball in the game Pong'''
        def __init__(self, vy, vx = (2*randint(0,1)-1)*VX/2.0, px=size[0]/2, py=size[1]/2, radius=ballRadius):
            self.px = px
            self.py = py
            self.vy = vy
            self.vx = vx
            self.radius = radius
            
        def paddleCollision(self, paddleObject):
            '''Computes the velocity of the ball after a collision with the paddle'''
            diff = self.py - paddleObject.y
            self.vy = diff/float(paddleLength)*maxVY
            self.vx = -self.vx/math.fabs(self.vx)*VX
            
        def sidewallCollision(self):
            self.vx = -self.vx
        
        def topwallCollision(self):
            self.vy = -self.vy
            
        def update(self):
            self.py += self.vy
            self.px += self.vx
            if self.py > size[1]-wallWidth-ballRadius or self.py < wallWidth+ballRadius:
                self.topwallCollision()
            if self.px > size[0]-wallWidth-ballRadius:
                if size[0]/2.0-goalLength/2.0<self.py<size[0]/2.0-goalLength/2.0:
                    if self.vx > 0:
                        self.sidewallCollision()
            if self.px < wallWidth+ballRadius:
                if size[0]/2.0-goalLength/2.0<self.py<size[0]/2.0-goalLength/2.0:
                    if self.vx < 0:
                        self.sidewallCollision()
                
    class Paddle:
        ''' Encodes the information from a paddle in the game Pong'''
        def __init__(self, user, x=300, y=size[1]/2, v=0, width=20):
            '''user attribute = 1 if paddle is a user's, otherwise 0'''
            self.user = user
            self.x = x
            self.y = y
            self.v = v
            self.width = width
            
        def update(self):
            if self.y < size[1]-paddleLength/2-wallWidth or self.v < 0:
                if self.y > paddleLength/2+wallWidth or self.v > 0:
                    self.y += self.v
                    
        def follow(self, ballObject):
            diff = ballObject.py - self.y
            if diff != 0:
                self.v = diff/ math.fabs(diff) * paddleSpeed
                
            
    class Model:
        '''Encodes the information of the state of a game of Pong'''
        def __init__(self, users, score1=0, score2=0, playAgain=2):
            self.users = users
            self.score1 = score1
            self.score2 = score2
            if player1Object == '0':
                self.user1 = User('')
            else:
                self.user1 = player1Object
            if player2Object == '0':
                self.user2 = User('')
            else:
                self.user2 = player2Object
            self.paddle1 = Paddle(1, size[0]-50)
            self.paddle2 = Paddle(self.users-1, 50)
            self.ball = Ball((2*random()-1)*maxVY/2.0)
            self.playAgain = playAgain
            
        def update(self):
            self.ball.update()
            if self.users == 1:
                self.paddle2.follow(self.ball)
            self.paddle1.update()
            self.paddle2.update()
            if self.paddle1.y-paddleLength/2-ballRadius < self.ball.py < self.paddle1.y+ballRadius+paddleLength/2:
                if self.paddle1.x-wallWidth-ballRadius < self.ball.px < self.paddle1.x+wallWidth+ballRadius:
                    if self.ball.vx > 0:
                        self.ball.paddleCollision(self.paddle1)
            if self.paddle2.y-paddleLength/2-ballRadius < self.ball.py < self.paddle2.y+ballRadius+paddleLength/2:
                if self.paddle2.x-wallWidth-ballRadius < self.ball.px < self.paddle2.x+wallWidth+ballRadius:
                    if self.ball.vx < 0:
                        self.ball.paddleCollision(self.paddle2)
            if self.ball.px < 0:
                self.scorePaddle1()
            if self.ball.px > size[0]:
                self.scorePaddle2()
            if self.ball.px < wallWidth + ballRadius:
                if self.ball.py < size[1]/2-goalLength/2 or self.ball.py > size[1]/2+goalLength/2:
                    if self.ball.vx < 0:
                        self.ball.sidewallCollision()
            if self.ball.px > size[0] - wallWidth - ballRadius:
                if self.ball.py < size[1]/2-goalLength/2 or self.ball.py > size[1]/2+goalLength/2:
                    if self.ball.vx > 0:
                        self.ball.sidewallCollision()
                    
                        
        def scorePaddle1(self):
            self.score1 += 1
            self.ball = Ball((2*random()-1)*maxVY/2.0)
            self.paddle1.y = size[1]/2
            self.paddle2.y = size[1]/2
            
        def scorePaddle2(self):
            self.score2 += 1
            self.ball = Ball((2*random()-1)*maxVY/2.0)
            self.paddle1.y = size[1]/2
            self.paddle2.y = size[1]/2
            
            
    class View:
        '''Renders the elements of the Pong Model'''
        def __init__(self, model, screen, animated=0):
            self.model = model
            self.screen = screen
            self.animated=animated
        
        def draw(self):
            self.screen.fill(pygame.Color(0,0,0))
            pygame.draw.rect(self.screen, (255,255,255), (size[0]/2-5, 0, wallWidth, size[1]))
            pygame.draw.rect(self.screen, (255,255,255), (0, 0, wallWidth, size[1]/2-goalLength/2))
            pygame.draw.rect(self.screen, (255,255,255), (0, size[1]/2+goalLength/2, wallWidth, size[1]/2-goalLength/2))
            pygame.draw.rect(self.screen, (255,255,255), (0, 0, size[0], wallWidth))
            pygame.draw.rect(self.screen, (255,255,255), (0, size[1]-wallWidth, size[0], wallWidth))
            pygame.draw.rect(self.screen, (255,255,255), (size[0]-wallWidth, 0, wallWidth, size[1]/2-goalLength/2))
            pygame.draw.rect(self.screen, (255,255,255), (size[0]-wallWidth, size[1]/2+goalLength/2, wallWidth, size[1]/2-goalLength/2))
            pygame.draw.rect(self.screen, (255,255,255), (self.model.paddle1.x-wallWidth/2.0, self.model.paddle1.y-paddleLength/2.0, wallWidth, paddleLength))
            pygame.draw.rect(self.screen, (255,255,255), (self.model.paddle2.x-wallWidth/2.0, self.model.paddle2.y-paddleLength/2.0, wallWidth, paddleLength))
            pygame.draw.circle(self.screen, (255,255,255), (int(self.model.ball.px), int(self.model.ball.py)), ballRadius)
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            msg = str(self.model.score1)
            msgSurfaceObj = fontObj.render(msg, False, (255,255,255))
            msgRectObj = self.screen.get_rect()
            msgRectObj.topleft = (3*size[0]/4.0,size[1]/10.0)
            screen.blit(msgSurfaceObj, msgRectObj)
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            msg = str(self.model.score2)
            msgSurfaceObj = fontObj.render(msg, False, (255,255,255))
            msgRectObj = self.screen.get_rect()
            msgRectObj.topleft = (size[0]/4.0,size[1]/10.0)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render(self.model.user1.name, False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (size[0]/2+10,size[1]+10)
            screen.blit(msgSurfaceObj, msgRectObj)     
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render(self.model.user2.name, False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,size[1]+10)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render('Wins: '+str(self.model.user2.win)+'   Losses: '+str(self.model.user2.loss), False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,size[1]+50)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render('Wins: '+str(self.model.user1.win)+'   Losses: '+str(self.model.user1.loss), False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (size[0]/2+10,size[1]+50)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            pygame.display.update()
            
        def win(self):
            self.screen.fill(pygame.Color(0,0,0))
            
            if self.animated != 1:
                self.animated = 1
                if self.model.score1>=winScore:
                    winner = self.model.user1.name
                    self.model.user1.win +=1
                    self.model.user2.loss+=1
                else:
                    winner = self.model.user2.name
                    self.model.user2.win +=1
                    self.model.user1.loss+=1
                
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                msgSurfaceObj = fontObj.render('CONGRATULATIONS, ', False, (255,0,0))
                msgRectObj = screen.get_rect()
                msgRectObj.topleft = (10,10)
                screen.blit(msgSurfaceObj, msgRectObj)
                
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                msgSurfaceObj = fontObj.render(winner, False, (255,0,0))
                msgRectObj = screen.get_rect()
                msgRectObj.topleft = (10,210)
                screen.blit(msgSurfaceObj, msgRectObj)
                
                fontObj = pygame.font.Font('freesansbold.ttf', 50)
                msgSurfaceObj = fontObj.render('WINS', False, (255,0,0))
                msgRectObj = screen.get_rect()
                msgRectObj.topleft = (10,410)
                screen.blit(msgSurfaceObj, msgRectObj)
                
                pygame.display.update()
                
                time.sleep(3)
            
            self.screen.fill(pygame.Color(0,0,0))
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render('Would these users like to play again?', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,10)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render('Press Enter to play again, N for new users, or ESC to exit', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,110)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            pygame.display.update()
        
        def lose(self):
            self.screen.fill(pygame.Color(0,0,0))
            
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            msgSurfaceObj = fontObj.render('THE', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,10)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            msgSurfaceObj = fontObj.render('COMPUTER', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,210)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 50)
            msgSurfaceObj = fontObj.render('WINS', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,410)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            pygame.display.update()
            
            time.sleep(3)
            
            self.screen.fill(pygame.Color(0,0,0))
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render('Would you like to play again?', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,10)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 20)
            msgSurfaceObj = fontObj.render('Press Enter to play again, N for new users, ESC to exit', False, (255,0,0))
            msgRectObj = screen.get_rect()
            msgRectObj.topleft = (10,110)
            screen.blit(msgSurfaceObj, msgRectObj)
            
            pygame.display.update()
            
    class Controller:
        def __init__(self, model):
            self.model = model
            
        def handle_pygame_event(self, event):
                if event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.model.paddle1.v = -paddleV
                    if event.key == pygame.K_DOWN:
                        self.model.paddle1.v = paddleV
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        self.model.playAgain = 1
                    if event.key == pygame.K_n:
                        users = 0
                        self.model.playAgain = 0
                    if self.model.users == 2:
                        if event.key == pygame.K_e:
                            self.model.paddle2.v = -paddleV
                        if event.key == pygame.K_d:
                            self.model.paddle2.v = paddleV
                elif event.type == KEYUP:
                    if event.key == pygame.K_UP:
                        self.model.paddle1.v = 0
                    if event.key == pygame.K_DOWN:
                        self.model.paddle1.v = 0
                    if self.model.users == 2:
                        if event.key == pygame.K_e:
                            self.model.paddle2.v = 0
                        if event.key == pygame.K_d:
                            self.model.paddle2.v = 0

    pygame.init()
    
    pygame.mixer.init()
    pygame.mixer.music.load("DropInTheOcean.mp3")
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1, 0.0)
    
    screen = pygame.display.set_mode((size[0], size[1]+100))
    
    screen.fill(pygame.Color(0,0,0))
    
    if users == 0:
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        msg = '1 or 2 players? Press 1 or 2'
        msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
        msgRectObj = screen.get_rect()
        msgRectObj.topleft = (10,200)
        screen.blit(msgSurfaceObj, msgRectObj)
        pygame.display.update()
        
        run = True
        while run:
            for event in pygame.event.get():
                if  event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_2:
                        users = 2
                        run = False
                    if event.key == pygame.K_1:
                        users = 1
                        run = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    
    model = Model(int(users))
    
    if player1Object == '0' and player2Object == '0':
        screen.fill(pygame.Color(0,0,0))
        
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        msg = 'Type your name, press Enter to Continue'
        msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
        msgRectObj = screen.get_rect()
        msgRectObj.topleft = (10,200)
        screen.blit(msgSurfaceObj, msgRectObj)
        pygame.display.update()
        
        run = True
        name1 = ''
        while run:
            for event in pygame.event.get():
                if  event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_s:
                        name1 += 'S'
                    if event.key == pygame.K_a:
                        name1 += 'A'
                    if event.key == pygame.K_b:
                        name1 += 'B'
                    if event.key == pygame.K_c:
                        name1 += 'C'
                    if event.key == pygame.K_d:
                        name1 += 'D'
                    if event.key == pygame.K_e:
                        name1 += 'E'
                    if event.key == pygame.K_f:
                        name1 += 'F'
                    if event.key == pygame.K_g:
                        name1 += 'G'
                    if event.key == pygame.K_h:
                        name1 += 'H'
                    if event.key == pygame.K_i:
                        name1 += 'I'
                    if event.key == pygame.K_j:
                        name1 += 'J'
                    if event.key == pygame.K_k:
                        name1 += 'K'
                    if event.key == pygame.K_l:
                        name1 += 'L'
                    if event.key == pygame.K_m:
                        name1 += 'M'
                    if event.key == pygame.K_n:
                        name1 += 'N'
                    if event.key == pygame.K_o:
                        name1 += 'O'
                    if event.key == pygame.K_p:
                        name1 += 'P'
                    if event.key == pygame.K_q:
                        name1 += 'Q'
                    if event.key == pygame.K_r:
                        name1 += 'R'
                    if event.key == pygame.K_t:
                        name1 += 'T'
                    if event.key == pygame.K_u:
                        name1 += 'U'
                    if event.key == pygame.K_v:
                        name1 += 'V'
                    if event.key == pygame.K_w:
                        name1 += 'W'
                    if event.key == pygame.K_x:
                        name1 += 'X'
                    if event.key == pygame.K_y:
                        name1 += 'Y'
                    if event.key == pygame.K_z:
                        name1 += 'Z'
                    if event.key == pygame.K_BACKSPACE:
                        name1 = name1[0:len(name1)-1]
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RETURN:
                        run = False
                
                screen.fill(pygame.Color(0,0,0))
                
                if users == 2:
                    fontObj = pygame.font.Font('freesansbold.ttf', 20)
                    msg = 'Person on the Right:'
                    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
                    msgRectObj = screen.get_rect()
                    msgRectObj.topleft = (10,180)
                    screen.blit(msgSurfaceObj, msgRectObj)              
                
                fontObj = pygame.font.Font('freesansbold.ttf', 20)
                msg = 'Type your name, press Enter to Continue'
                msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
                msgRectObj = screen.get_rect()
                msgRectObj.topleft = (10,200)
                screen.blit(msgSurfaceObj, msgRectObj)                   
                        
                fontObj = pygame.font.Font('freesansbold.ttf', 20)
                msgSurfaceObj = fontObj.render(name1, False, (255,0,0))
                msgRectObj = screen.get_rect()
                msgRectObj.topleft = (10,250)
                screen.blit(msgSurfaceObj, msgRectObj)
                pygame.display.update()
                
        model.user1.name = name1
        
        if users == 2:
            run = True
            name2 = ''
            while run:
                for event in pygame.event.get():
                    if  event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == pygame.K_s:
                            name2 += 'S'
                        if event.key == pygame.K_a:
                            name2 += 'A'
                        if event.key == pygame.K_b:
                            name2 += 'B'
                        if event.key == pygame.K_c:
                            name2 += 'C'
                        if event.key == pygame.K_d:
                            name2 += 'D'
                        if event.key == pygame.K_e:
                            name2 += 'E'
                        if event.key == pygame.K_f:
                            name2 += 'F'
                        if event.key == pygame.K_g:
                            name2 += 'G'
                        if event.key == pygame.K_h:
                            name2 += 'H'
                        if event.key == pygame.K_i:
                            name2 += 'I'
                        if event.key == pygame.K_j:
                            name2 += 'J'
                        if event.key == pygame.K_k:
                            name2 += 'K'
                        if event.key == pygame.K_l:
                            name2 += 'L'
                        if event.key == pygame.K_m:
                            name2 += 'M'
                        if event.key == pygame.K_n:
                            name2 += 'N'
                        if event.key == pygame.K_o:
                            name2 += 'O'
                        if event.key == pygame.K_p:
                            name2 += 'P'
                        if event.key == pygame.K_q:
                            name2 += 'Q'
                        if event.key == pygame.K_r:
                            name2 += 'R'
                        if event.key == pygame.K_t:
                            name2 += 'T'
                        if event.key == pygame.K_u:
                            name2 += 'U'
                        if event.key == pygame.K_v:
                            name2 += 'V'
                        if event.key == pygame.K_w:
                            name2 += 'W'
                        if event.key == pygame.K_x:
                            name2 += 'X'
                        if event.key == pygame.K_y:
                            name2 += 'Y'
                        if event.key == pygame.K_z:
                            name2 += 'Z'
                        if event.key == pygame.K_BACKSPACE:
                            name2 = name2[0:len(name2)-1]
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        if event.key == pygame.K_RETURN:
                            run = False
                            
                    screen.fill(pygame.Color(0,0,0))
                    
                    fontObj = pygame.font.Font('freesansbold.ttf', 20)
                    msg = 'Person on the Left:'
                    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
                    msgRectObj = screen.get_rect()
                    msgRectObj.topleft = (10,180)
                    screen.blit(msgSurfaceObj, msgRectObj)  
                
                    fontObj = pygame.font.Font('freesansbold.ttf', 20)
                    msg = 'Type your name, press Enter to Continue'
                    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
                    msgRectObj = screen.get_rect()
                    msgRectObj.topleft = (10,200)
                    screen.blit(msgSurfaceObj, msgRectObj)
                    pygame.display.update()                       
                            
                    fontObj = pygame.font.Font('freesansbold.ttf', 20)
                    msgSurfaceObj = fontObj.render(name2, False, (255,0,0))
                    msgRectObj = screen.get_rect()
                    msgRectObj.topleft = (10,250)
                    screen.blit(msgSurfaceObj, msgRectObj)
                    pygame.display.update()
                    
            model.user2.name = name2
        else:
            model.user2.name = 'COMPUTER'
                        
    screen.fill(pygame.Color(0,0,0))
    
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    msg = 'Player One moves with the Up and Down Arrows'
    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
    msgRectObj = screen.get_rect()
    msgRectObj.topleft = (10,200)
    screen.blit(msgSurfaceObj, msgRectObj)
    if users == 2:
        fontObj = pygame.font.Font('freesansbold.ttf', 20)
        msg = 'Player Two moves with the D and E keys'
        msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
        msgRectObj = screen.get_rect()
        msgRectObj.topleft = (10,250)
        screen.blit(msgSurfaceObj, msgRectObj)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    msg = 'Dodge their balls while hitting them with yours'
    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
    msgRectObj = screen.get_rect()
    msgRectObj.topleft = (10,300)
    screen.blit(msgSurfaceObj, msgRectObj)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    msg = 'Press Enter to continue'
    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
    msgRectObj = screen.get_rect()
    msgRectObj.topleft = (10,400)
    screen.blit(msgSurfaceObj, msgRectObj)
    
    pygame.display.update()        
    run = True
    while run:
        for event in pygame.event.get():
            if  event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
    pygame.display.set_caption("Pong Game")
    controller = Controller(model)
    view = View(model, screen)
    
    while True:
        for event in pygame.event.get():
            if  event.type == QUIT:
                pygame.quit()
                sys.exit()
            controller.handle_pygame_event(event)
        if users == 1:
            if model.score1 >= winScore:
                view.win()
            elif model.score2 >= winScore:
                view.lose()
            else:
                model.update()
                view.draw()
        elif users == 2:
            if model.score1 >= winScore:
                view.win()
            elif model.score2 >= winScore:
                view.win()
            else:
                model.update()
                view.draw()
        if model.playAgain == 1:
            runAgain = True
            player1Object = model.user1
            player2Object = model.user2
            return (runAgain, users, player1Object, player2Object)
        if model.playAgain == 0:
            runAgain = True
            users = 0
            player1Object = '0'
            player2Object = '0'
            return (runAgain, users, player1Object, player2Object)
        time.sleep(.001)
    
x = game(0,'0','0')
while x[0]:
    print x
    print x[2]
    print x[3]
    x=game(x[1], x[2], x[3])

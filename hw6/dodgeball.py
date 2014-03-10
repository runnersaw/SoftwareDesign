# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 15:01:03 2014

@author: sawyer
"""

if __name__ == '__main__':
    import pygame, sys
    import pygame.camera
    from pygame.locals import *
    from random import *
    import time
    import math
    import sys
    
def game():
    '''This function runs the whole game. This is in the form of a function 
    so that the user can play multiple times in the loop at the end of this
    script '''
    hitSounds=['opponenthit1.ogg', 'opponenthit2.ogg', 'opponenthit3.ogg', 'opponenthit4.ogg', 'opponenthit5.ogg']
    loseSounds=['lose1.ogg', 'loss2.ogg']
    startSounds=['start.ogg', 'start2.ogg']
    size = (800,800) #size of the game screen
    playerSize = (80,60) #size of the player sprites
    cooldownTime = 500 # in ms, the time before computers can throw again
    userCooldown = 1500 #in ms, the time before the user can throw again
    ballSpeed = 3.5 # in pixels per ms, speed of balls
    ballRadius = 10 #in pixels
    AIrefresh = 100 # in milliseconds, time before they switch directions
    userSpeed = 1.5 # in pixels per ms, speed of user
    
    class Ball:
        ''' This class encodes all the information for balls. It encodes their position and velocity. '''
        def __init__(self, px, py, vx, vy, color=(255,255,255),alive =1):
            '''specifies position and velocity of balls, and also whether they are displayed '''
            self.px = px
            self.py = py
            self.vx = vx
            self.vy = vy
            self.color = color
            self.alive = alive
            
        def update(self):
            self.px += self.vx
            self.py += self.vy
        
        def throw(self):
            if self.py >= 4*size[1]/9:
                self.vy = -ballSpeed #throws the ball upward if the ball is below the middle
            elif self.py <= 5*size[1]/9:
                self.vy = ballSpeed #throws the ball downward if the ball is above the middle
                
        def collision(self):
            self.alive = 0 #makes the ball not display
            self.vy = 0 #makes the ball not collide with anything else
                
    class CPU:
        ''' This class encodes all the information for a single person. This person may be the user or an AI. '''
        def __init__(self, py=size[1]/2, px=size[0]/2, vx=0, vy=0, cooldown=0, hasball=1, ball=0, alive=1):
            ''' Specifies position, velocity, time since last throw, whether they have a ball,
            and a ball attribute of their own. '''            
            self.px = px
            self.py = py
            self.vx = vx
            self.vy = vy
            self.cooldown=cooldown
            self.hasball = hasball
            self.ball = Ball(px, py, vx, vy)
            self.alive = alive
            
        def update(self):
            if not 0<=self.px<=size[0]-playerSize[0]:
                self.vx = -self.vx #reflects off the wall
            self.px += self.vx
            self.py += self.vy
            if self.hasball == 1: #if player is carrying ball, makes it stay with player
                self.ball.px = self.px+playerSize[0]/2
                self.ball.py = self.py+playerSize[1]            
                self.ball.vx = self.vx
                self.ball.vy = self.vy
            self.ball.update()
            
                
        def AIupdate(self):
            ''' This function refreshes the AI's velocity and whether he throws a ball
            in the period specified by the variable AIrefresh. '''
            self.cooldown += AIrefresh+1 #function is called every AIrefresh, so that much time has passed
            self.vx = randint(-3, 3)/2 #random velic
            if self.cooldown >= cooldownTime: # if he has waited the cooldown period
                if self.hasball != 1: # if he doesn't have a ball
                    self.ball = Ball(self.px, self.py, self.vx, self.vy) # he gets a ball attribute
                    self.hasball = 1 
            if self.hasball == 1:
                thrown = randint(1, 4)
                if thrown == 1: #chooses whether to throw the ball
                    if self.alive == 1:
                        self.ball.throw()
                        self.hasball = 0
                        self.cooldown = 0
       
        def collision(self):
            '''This function specifies what the opponent does if they are hit. '''
            self.alive = 0
            #this section plays a random sound that we recorded for hits:
            num = randint(0, len(hitSounds)-1)
            sound = pygame.mixer.Sound(hitSounds[num])
            sound.play()
        
    class User:
        ''' This class encodes all the information for a single person. This person may be the user or an AI. '''
        def __init__(self, py=size[1]/2, px=size[0]/2, vx=0, vy=0, cooldown=0, genball=0, hasball=1, ball=0, alive = 1):
            ''' initalizes the user's position, velocity and ball, and also cooldown time. '''            
            self.px = px
            self.py = py
            self.vx = vx
            self.vy = vy
            self.cooldown = cooldown
            self.hasball = hasball #specifies whether the user has picked up the ball
            self.ball = Ball(px, py, vx, vy)
            self.alive = alive
            self.genball = genball #this specifies whether a ball has been generated but not picked up
            
        def update(self):
            if self.px<=0:
                if self.vx<0:
                    self.vx = 0
            elif self.px >= size[0]-playerSize[0]:
                if self.vx>0:
                    self.vx = 0
            if self.py>=size[1]-playerSize[1]:
                if self.vy > 0:
                    self.vy = 0
            if self.py<=size[1]/2:
                if self.vy < 0:
                    self.vy = 0
            self.px += self.vx
            self.py += self.vy
            self.cooldown += 1
            #this section generates a ball if there isn't one on the field
            if self.cooldown >= userCooldown: # if he has waited the cooldown period
                if self.genball != 1: # if no ball has been generated
                    if self.hasball != 1:
                        self.genball = 1
                        self.ball = Ball(randint(0,size[0]), randint(size[1]/2, size[1]), 0, 0) # he gets a ball attribute
            #section tests whether he's picked up a ball
            if self.genball == 1:
                if (self.px-ballRadius)<= self.ball.px <=(self.px+playerSize[0]+ballRadius):
                    if (self.py-ballRadius)<= self.ball.py <=(self.py+playerSize[1]+ballRadius):
                        self.hasball = 1
                        self.genball = 0
            #section forces the ball to stay with the player
            if self.hasball == 1:
                self.ball.px = self.px+playerSize[0]/2
                self.ball.py = self.py
                self.ball.vx = self.vx
                self.ball.vy = self.vy
            self.ball.update()
        
        def userThrow(self):
            if self.hasball == 1: #can only throw if he has a ball
                self.ball.throw()
                self.hasball = 0 #no longer has a ball
                self.cooldown = 0
                
        def collision(self):
            self.alive = 0
            self.ball.alive = 0
            #plays a sound if you are hit, which means you lose
            num = randint(0, len(loseSounds)-1)
            sound = pygame.mixer.Sound(loseSounds[num])
            sound.play()
    
    class Model:
        ''' This class is the model for our dodgeball game. It encodes all the information such as the locations and velocities of all the elements in the game '''
        def __init__(self, playAgain=0):
            self.opponent1 = CPU(1*size[1]/20,size[0]*randint(1,6)/7)
            self.opponent2 = CPU(3*size[1]/20,size[0]*randint(1,6)/7)
            self.opponent3 = CPU(5*size[1]/20,size[0]*randint(1,6)/7)
            self.user = User(7*size[1]/8)
            self.victory = 0
            self.playAgain=playAgain
        
        def update(self):
            if pygame.time.get_ticks()%AIrefresh == 0:
                self.opponent1.AIupdate()
                self.opponent2.AIupdate()
                self.opponent3.AIupdate()
            self.user.update()
            self.opponent1.update()
            self.opponent2.update()
            self.opponent3.update()
            #this section detects collisions
            if (self.user.px-ballRadius)<= self.opponent1.ball.px <=(self.user.px+playerSize[0]+ballRadius):
                if (self.user.py-ballRadius)<= self.opponent1.ball.py <=(self.user.py+playerSize[1]+ballRadius):
                    if self.opponent1.alive == 1:
                        self.user.collision()
                        self.opponent1.ball.collision()
            if (self.user.px-ballRadius)<= self.opponent2.ball.px <=(self.user.px+playerSize[0]+ballRadius):
                if (self.user.py-ballRadius)<= self.opponent2.ball.py <=(self.user.py+playerSize[1]+ballRadius):
                    if self.opponent2.alive == 1:
                        self.user.collision()
                        self.opponent2.ball.collision()
            if (self.user.px-ballRadius)<= self.opponent3.ball.px <=(self.user.px+playerSize[0]+ballRadius):
                if (self.user.py-ballRadius)<= self.opponent3.ball.py <=(self.user.py+playerSize[1]+ballRadius):
                    if self.opponent3.alive == 1:
                        self.user.collision()
                        self.opponent3.ball.collision()
            if self.opponent1.alive == 1:
                if (self.opponent1.px-ballRadius)<= self.user.ball.px <=(self.opponent1.px+playerSize[0]+ballRadius):
                    if (self.opponent1.py-ballRadius)<= self.user.ball.py <=(self.opponent1.py+playerSize[1]+ballRadius):
                        self.opponent1.collision()
                        self.user.ball.collision()
            if self.opponent2.alive == 1:
                if (self.opponent2.px-ballRadius)<= self.user.ball.px <=(self.opponent2.px+playerSize[0]+ballRadius):
                    if (self.opponent2.py-ballRadius)<= self.user.ball.py <=(self.opponent2.py+playerSize[1]+ballRadius):
                        self.opponent2.collision()
                        self.user.ball.collision()
            if self.opponent3.alive == 1:
                if (self.opponent3.px-ballRadius)<= self.user.ball.px <=(self.opponent3.px+playerSize[0]+ballRadius):
                    if (self.opponent3.py-ballRadius)<= self.user.ball.py <=(self.opponent3.py+playerSize[1]+ballRadius):
                        self.opponent3.collision()
                        self.user.ball.collision()
            # this section detects victory and loss conditions
            if self.opponent1.alive == 0 and self.opponent2.alive == 0 and self.opponent3.alive == 0:
                if self.victory !=1:
                    self.victory = 1
            if self.user.alive == 0:
                self.victory = 2
                    
            
                    
            
    class View:
        ''' This class takes the information stored in the model and displays it for the user. '''
        def __init__(self, model, screen):
            self.model = model
            self.screen = screen
    
        def draw(self):
            ''' This function takes the information in the model and draws it '''
            self.screen.fill(pygame.Color(0,0,0))
            pygame.draw.rect(self.screen, (255,255,255), (0, size[1]/2-5, size[0], 10))
            
            #These check to see if user is still alive before drawing them
            if self.model.user.alive == 1:   
                self.screen.blit(player, (self.model.user.px, self.model.user.py))
                if self.model.user.ball.alive == 1:
                    pygame.draw.circle(self.screen, self.model.user.ball.color, (int(self.model.user.ball.px), int(self.model.user.ball.py)), ballRadius)
            if self.model.opponent1.alive == 1:          
                self.screen.blit(opponent1, (self.model.opponent1.px, self.model.opponent1.py))
                if self.model.opponent1.ball.alive == 1:
                    pygame.draw.circle(self.screen, self.model.opponent1.ball.color, (int(self.model.opponent1.ball.px), int(self.model.opponent1.ball.py)), ballRadius)
            if self.model.opponent2.alive == 1:  
                self.screen.blit(opponent2, (self.model.opponent2.px, self.model.opponent2.py))
                if self.model.opponent2.ball.alive == 1:
                    pygame.draw.circle(self.screen, self.model.opponent2.ball.color, (int(self.model.opponent2.ball.px), int(self.model.opponent2.ball.py)), ballRadius)
            if self.model.opponent3.alive == 1:  
                self.screen.blit(opponent3, (self.model.opponent3.px, self.model.opponent3.py))
                if self.model.opponent3.ball.alive == 1:
                    pygame.draw.circle(self.screen, self.model.opponent3.ball.color, (int(self.model.opponent3.ball.px), int(self.model.opponent3.ball.py)), ballRadius)
            pygame.display.update()
            
        def win(self):
            time.sleep(1) #for aesthetics
            #this section fills text for winning
            self.screen.fill(pygame.Color(0,0,0))
            
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            msg = 'CONGRATULATIONS, YOU MANAGED TO WIN'
            msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
            msgRectObj = self.screen.get_rect()
            msgRectObj.topleft = (10,20)
            self.screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            msg = 'ENTER TO TRY AGAIN, ESC TO QUIT'
            msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
            msgRectObj = self.screen.get_rect()
            msgRectObj.topleft = (10,200)
            self.screen.blit(msgSurfaceObj, msgRectObj)
            
            pygame.display.update()
        
        def loss(self):
            time.sleep(1) #for aesthetics
            #this section fills text for losing
            self.screen.fill(pygame.Color(0,0,0))
            
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            msg = 'YOU LOSE'
            msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
            msgRectObj = self.screen.get_rect()
            msgRectObj.topleft = (10,20)
            self.screen.blit(msgSurfaceObj, msgRectObj)
            
            fontObj = pygame.font.Font('freesansbold.ttf', 32)
            msg = 'ENTER TO TRY AGAIN, ESC TO QUIT'
            msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
            msgRectObj = self.screen.get_rect()
            msgRectObj.topleft = (10,200)
            self.screen.blit(msgSurfaceObj, msgRectObj)
            
            pygame.display.update()
            
    
    class keyController:
        ''' This class takes the input from the user and converts that to changes in the information of the program, for example changing the user's velocity. '''
        def __init__(self, model):
            self.model = model
             
        def handle_pygame_event(self, event):
            if event.type == KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.model.user.vx = userSpeed
                if event.key == pygame.K_LEFT:
                    self.model.user.vx = -userSpeed
                if event.key == pygame.K_UP:
                    self.model.user.vy = -userSpeed
                if event.key == pygame.K_DOWN:
                    self.model.user.vy = userSpeed
                if event.key == pygame.K_SPACE:
                    self.model.user.userThrow()
                if event.key == pygame.K_RETURN:
                    self.model.playAgain = 1
                if event.key == pygame.K_ESCAPE:
                    self.model.playAgain = -1
            elif event.type == KEYUP:
                if event.key == pygame.K_RIGHT:
                    if self.model.user.vx >0:
                        self.model.user.vx = 0
                if event.key == pygame.K_LEFT:
                    if self.model.user.vx <0:
                        self.model.user.vx = 0
                if event.key == pygame.K_UP:
                    if self.model.user.vy <0:
                        self.model.user.vy = 0
                if event.key == pygame.K_DOWN:
                    if self.model.user.vy >0:
                        self.model.user.vy = 0
            
      
    
    	
     #Initializing lots of important sruff  
    pygame.init()
    pygame.camera.init()
    pygame.mixer.init()
    pygame.mixer.music.load("eyeTiger.mp3")
    pygame.mixer.music.set_volume(.1)
    pygame.mixer.music.play(-1, 0.0)
    
    pygame.display.set_caption("Dodgeball")
    screen = pygame.display.set_mode(size)   
    
    #this section counts down and takes the user's picture to use as their sprite
    for i in range(300):
        screen.fill(pygame.Color(0,0,0))
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        msg = 'Smile for your picture. It will be taken in:'
        msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
        msgRectObj = screen.get_rect()
        msgRectObj.topleft = (10,20)
        screen.blit(msgSurfaceObj, msgRectObj)
        
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        x = (400-i)/100
        msg = str(x)
        msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
        msgRectObj = screen.get_rect()
        msgRectObj.topleft = (10,200)
        screen.blit(msgSurfaceObj, msgRectObj)
        
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        msg = 'The picture will be used as your sprite'
        msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
        msgRectObj = screen.get_rect()
        msgRectObj.topleft = (10,400)
        screen.blit(msgSurfaceObj, msgRectObj)
        
        pygame.display.update()         
        time.sleep(.008)
    
    cam = pygame.camera.Camera("/dev/video0",(20,20))
    cam.start()
    pygame.image.save(cam.get_image(), "image.jpg")
    cam.stop()
    
    #this section gives instructions
    screen.fill(pygame.Color(0,0,0))
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    msg = 'Instructions: Use the arrow keys to move, and throw with the space bar'
    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
    msgRectObj = screen.get_rect()
    msgRectObj.topleft = (10,200)
    screen.blit(msgSurfaceObj, msgRectObj)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    msg = 'Dodge their balls while hitting them with yours'
    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
    msgRectObj = screen.get_rect()
    msgRectObj.topleft = (10,300)
    screen.blit(msgSurfaceObj, msgRectObj)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    msg = 'Pick up the balls on your side of the court to reload'
    msgSurfaceObj = fontObj.render(msg, False, (255,0,0))
    msgRectObj = screen.get_rect()
    msgRectObj.topleft = (10,400)
    screen.blit(msgSurfaceObj, msgRectObj)
    
    pygame.display.update()        
    time.sleep(5)
    
    #this section plays a start sound
    num = randint(0, len(startSounds)-1)
    sound = pygame.mixer.Sound(startSounds[num])
    sound.play()
    
    #List of potential enemy sprites
    sprites = []
    sprites.append(pygame.image.load('griffin.jpg'))
    sprites.append(pygame.image.load('nala.jpg'))
    sprites.append(pygame.image.load('nick-tatar.jpg'))
    sprites.append(pygame.image.load('ruvolo_olin_mug.jpg'))
    sprites.append(pygame.image.load('sawyer.jpg'))
    sprites.append(pygame.image.load('whiteGoodman.jpg'))
    
    #generates random integers to pick enemy sprites
    rand1 = randint(0, 5)
    rand2 = randint(0, 5)
    rand3 = randint(0, 5)
    while rand1 == rand2:
    	rand2 = randint(0, 5)
    while rand3 == rand1 or rand3 == rand2:
    	rand3 = randint(0, 5)
    
    #Load all the players and opponents and resize them to the proper size
    player = pygame.image.load("image.jpg")   
    player = pygame.transform.scale(player, (playerSize))
    
    opponent1 = sprites[rand1] 
    opponent1 = pygame.transform.scale(opponent1, (playerSize))
    
    opponent2 = sprites[rand2]  
    opponent2 = pygame.transform.scale(opponent2, (playerSize))
    
    opponent3 = sprites[rand3]  
    opponent3 = pygame.transform.scale(opponent3, (playerSize))
    
    screen = pygame.display.set_mode(size)
    
    model = Model()
    view = View(model, screen)
    controller = keyController(model)
    
    #runs the game
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            controller.handle_pygame_event(event)
        model.update()
        if model.victory == 0:
            view.draw()
        elif model.victory == 1:
            view.win()
            if model.playAgain == 1:
                return True
            if model.playAgain == -1:
                return False
        elif model.victory == 2:
            view.loss()
            if model.playAgain == 1:
                return True
            if model.playAgain == -1:
                return False
        time.sleep(.001)
                
#this is a loop so that the player can choose to play the game again after they're done
if __name__ == '__main__':
    x=True
    while x:
        x=game()

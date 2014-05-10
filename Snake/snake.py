import pygame
from pygame.locals import *
import random
import math
import time


class SnakeWorld:
    def __init__(self):
        """Initializes the SnakeWorld game.  Creates two heads, one food, and the board."""
        self.font = pygame.font.Font('freesansbold.ttf',30)
        self.font2 = pygame.font.Font('freesansbold.ttf',18)
        self.font3 = pygame.font.Font('freesansbold.ttf',22)
        self.blocks=[] #Intialise the list of all blocks wich make up the board
        self.tails=[] #Initializes the list for tails for the first head
        self.tails2=[] #and the second head
        self.score=0 #Player 1/head 1 score
        self.score2=0 #Player 2/hed 2 score
        self.xcoor=[] #List of all x-coordinates that head1 has had in order
        self.ycoor=[] #List of all y-coordinates that head 1 has had in order
        self.xcoor2=[] #and head 2 x-coordinates
        self.ycoor2=[] #and head 2 y-coordinates
        for x in range(10,630,10): #This loop adds all the blocks which make up the game board
              for y in range(10,470,10):
                  block = Block((255,255,255),10,10,x,y) #Creates one instance of the Block object
                  self.blocks.append(block) #Adds the instance to the list of all blocks
        self.food=Food((0,255,0),10,10,random.randrange(10,630,10),random.randrange(10,470,10)) #Adds a food dot with random (x,y) coordinates within the game board
        self.head=Head((0,0,255),10,10,340,240,10,0) #Creates the first head at the center moving right initially
        self.headRect=pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height) #stores the rectangle location of the head's current position
        self.head2=Head((255,0,0),10,10,330,240,-10,0) #head2 moves left initially
        self.head2Rect=pygame.Rect(self.head2.x,self.head2.y,self.head2.width,self.head2.height) #same as head1 for head 2
        self.foodRect=pygame.Rect(self.food.x-1,self.food.y-1,self.food.width-1,self.food.height-1) #stores the rectangle of the food location
        self.boardRect=pygame.Rect(10,10,620,460)
        self.flag = False        
        
    def update(self):
        self.xcoor.append(self.head.x)
        self.ycoor.append(self.head.y)
        self.xcoor2.append(self.head2.x)
        self.ycoor2.append(self.head2.y)
        self.head.update()
        self.headRect=pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height)
        
        if self.headRect.colliderect(self.head2Rect):
            self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
            self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
            self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
            if self.score>self.score2:
                self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
            elif self.score==self.score2:
                self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
            elif self.score<self.score2:
                self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
            self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
            self.msgRect = self.msgObject.get_rect()
            self.msgRect2 = self.msgObject2.get_rect()
            self.msgRect25 = self.msgObject25.get_rect()
            self.msgRect255 = self.msgObject255.get_rect()
            self.msgRect3 = self.msgObject3.get_rect()
            self.msgRect.topleft = (200,160)
            self.msgRect2.topleft = (200,250)
            self.msgRect25.topleft = (200,280)
            self.msgRect255.topleft = (200,300)
            self.msgRect3.topleft = (200,330)
            self.flag = True
        else:
            pass
        
        self.head2.update()        
        self.head2Rect=pygame.Rect(self.head2.x,self.head2.y,self.head2.width,self.head2.height)
        self.foodRect=pygame.Rect(self.food.x,self.food.y,self.food.width,self.food.height)
        
        if self.headRect.colliderect(self.foodRect):
            self.food.update(random.randrange(10,630,10),random.randrange(10,470,10))
            tail=Tail((0,0,200),10,10,self.head.x,self.head.y)
            self.tails.append(tail)
        else:
            pass
        
        if self.head2Rect.colliderect(self.foodRect):
            self.food.update(random.randrange(10,630,10),random.randrange(10,470,10))
            tail=Tail((200,0,0),10,10,self.head2.x,self.head2.y)
            self.tails2.append(tail)
        else:
            pass
        
        self.score=len(self.tails)
        self.score2=len(self.tails2)
        i=1
        j=5
        for tail in self.tails:
            tail.update(self.xcoor[-i],self.ycoor[-i],(j,0,200-j))
            i+=1
            if i<40:
                j=i*5
            elif j<10:
                j+=5
            else:
                j-=5
        i=1
        j=5
        for tail in self.tails2:
            tail.update(self.xcoor2[-i],self.ycoor2[-i],(200-j,0,j))
            i+=1
            if i<40:
                j=i*5
            elif j<10:
                j+=5
            else:
                j-=5        
        
        if self.headRect.colliderect(self.head2Rect):
            self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
            self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
            self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
            if self.score>self.score2:
                self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
            elif self.score==self.score2:
                self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
            elif self.score<self.score2:
                self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
            self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
            self.msgRect = self.msgObject.get_rect()
            self.msgRect2 = self.msgObject2.get_rect()
            self.msgRect25 = self.msgObject25.get_rect()
            self.msgRect255 = self.msgObject255.get_rect()
            self.msgRect3 = self.msgObject3.get_rect()
            self.msgRect.topleft = (200,160)
            self.msgRect2.topleft = (200,250)
            self.msgRect25.topleft = (200,280)
            self.msgRect255.topleft = (200,300)
            self.msgRect3.topleft = (200,330)
            self.flag = True
        else:
            pass
        
        for tail in self.tails:
            tailrect = pygame.Rect(tail.x,tail.y,tail.width,tail.height)
            if self.headRect.colliderect(tailrect):
                self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
                self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
                self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
                if self.score>self.score2:
                    self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
                elif self.score==self.score2:
                    self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
                elif self.score<self.score2:
                    self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
                self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
                self.msgRect = self.msgObject.get_rect()
                self.msgRect2 = self.msgObject2.get_rect()
                self.msgRect25 = self.msgObject25.get_rect()
                self.msgRect255 = self.msgObject255.get_rect()
                self.msgRect3 = self.msgObject3.get_rect()
                self.msgRect.topleft = (200,160)
                self.msgRect2.topleft = (200,250)
                self.msgRect25.topleft = (200,280)
                self.msgRect255.topleft = (200,300)
                self.msgRect3.topleft = (200,330)
                self.flag = True
                break
            else:
                pass
          
            if self.head2Rect.colliderect(tailrect):
                self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
                self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
                self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
                if self.score>self.score2:
                    self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
                elif self.score==self.score2:
                    self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
                elif self.score<self.score2:
                    self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
                self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
                self.msgRect = self.msgObject.get_rect()
                self.msgRect2 = self.msgObject2.get_rect()
                self.msgRect25 = self.msgObject25.get_rect()
                self.msgRect255 = self.msgObject255.get_rect()
                self.msgRect3 = self.msgObject3.get_rect()
                self.msgRect.topleft = (200,160)
                self.msgRect2.topleft = (200,250)
                self.msgRect25.topleft = (200,280)
                self.msgRect255.topleft = (200,300)
                self.msgRect3.topleft = (200,330)
                self.flag = True
                break
            else:
                pass
        
        for tail in self.tails2:
            tailrect = pygame.Rect(tail.x,tail.y,tail.width,tail.height)
            if self.headRect.colliderect(tailrect):
                self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
                self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
                self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
                if self.score>self.score2:
                    self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
                elif self.score==self.score2:
                    self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
                elif self.score<self.score2:
                    self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
                self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
                self.msgRect = self.msgObject.get_rect()
                self.msgRect2 = self.msgObject2.get_rect()
                self.msgRect25 = self.msgObject25.get_rect()
                self.msgRect255 = self.msgObject255.get_rect()
                self.msgRect3 = self.msgObject3.get_rect()
                self.msgRect.topleft = (200,160)
                self.msgRect2.topleft = (200,250)
                self.msgRect25.topleft = (200,280)
                self.msgRect255.topleft = (200,300)
                self.msgRect3.topleft = (200,330)
                self.flag = True
                break
            else:
                pass
            if self.head2Rect.colliderect(tailrect):
                self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
                self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
                self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
                if self.score>self.score2:
                    self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
                elif self.score==self.score2:
                    self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
                elif self.score<self.score2:
                    self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
                self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
                self.msgRect = self.msgObject.get_rect()
                self.msgRect2 = self.msgObject2.get_rect()
                self.msgRect25 = self.msgObject25.get_rect()
                self.msgRect255 = self.msgObject255.get_rect()
                self.msgRect3 = self.msgObject3.get_rect()
                self.msgRect.topleft = (200,160)
                self.msgRect2.topleft = (200,250)
                self.msgRect25.topleft = (200,280)
                self.msgRect255.topleft = (200,300)
                self.msgRect3.topleft = (200,330)
                self.flag = True
                break
            else:
                pass        
        
        if self.headRect.colliderect(self.boardRect):
            pass
        else:
            self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
            self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
            self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
            if self.score>self.score2:
                self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
            elif self.score==self.score2:
                self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
            elif self.score<self.score2:
                self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
            self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
            self.msgRect = self.msgObject.get_rect()
            self.msgRect2 = self.msgObject2.get_rect()
            self.msgRect25 = self.msgObject25.get_rect()
            self.msgRect255 = self.msgObject255.get_rect()
            self.msgRect3 = self.msgObject3.get_rect()
            self.msgRect.topleft = (200,160)
            self.msgRect2.topleft = (200,250)
            self.msgRect25.topleft = (200,280)
            self.msgRect255.topleft = (200,300)
            self.msgRect3.topleft = (200,330)
            self.flag = True
            
        if self.head2Rect.colliderect(self.boardRect):
            pass
        else:
            self.msgObject = self.font.render('GAME OVER',False,(0,0,255))
            self.msgObject2 = self.font2.render('P1 Score was: '+str(self.score),False,(125,125,125))
            self.msgObject25 = self.font2.render('P2 Score was: ' + str(self.score2),False,(125,125,125))
            if self.score>self.score2:
                self.msgObject255 = self.font2.render('P1 Wins',False,(125,125,125))
            elif self.score==self.score2:
                self.msgObject255 = self.font2.render('It is a Tie',False,(125,125,125))
            elif self.score<self.score2:
                self.msgObject255 = self.font2.render('P2 Wins',False,(125,125,125))
            self.msgObject3 = self.font3.render('Press Enter to Play a New Game',False,(0,0,0))
            self.msgRect = self.msgObject.get_rect()
            self.msgRect2 = self.msgObject2.get_rect()
            self.msgRect25 = self.msgObject25.get_rect()
            self.msgRect255 = self.msgObject255.get_rect()
            self.msgRect3 = self.msgObject3.get_rect()
            self.msgRect.topleft = (200,160)
            self.msgRect2.topleft = (200,250)
            self.msgRect25.topleft = (200,280)
            self.msgRect255.topleft = (200,300)
            self.msgRect3.topleft = (200,330)
            self.flag = True
       

    def reset(self):
        self.tails=[]
        self.tails2=[]
        self.score=0
        self.score2=0
        self.highscore=0
        self.xcoor=[]
        self.ycoor=[]
        self.xcoor2=[]
        self.ycoor2=[]
        self.food=Food((0,255,0),10,10,random.randrange(10,630,10),random.randrange(10,470,10))
        self.head=Head((0,0,255),10,10,340,240,10,0)
        self.headRect=pygame.Rect(self.head.x,self.head.y,self.head.width,self.head.height)
        self.head2=Head((255,0,0),10,10,340,240,(-10),0)
        self.head2Rect=pygame.Rect(self.head2.x,self.head2.y,self.head2.width,self.head2.height)
        self.foodRect=pygame.Rect(self.food.x,self.food.y,self.food.width,self.food.height)
        self.flag = False        

class Block:
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
    
class Head:
    def __init__(self,color,height,width,x,y,vx,vy):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.vx=vx
        self.vy=vy
    
    def update(self):
        self.x+=self.vx
        self.y+=self.vy
    
class Tail:
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        
    def update(self,coorx,coory,color):
        self.x = coorx
        self.y = coory
        self.color=color
    
class Food:
    """This Defines the food Object for the Game""" 
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y 
        
    def update(self,newx,newy):
        self.x = newx
        self.y = newy
        
class PyGameWindowView:
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen
    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        for block in self.model.blocks:
            pygame.draw.rect(self.screen, pygame.Color(block.color[0],block.color[1],block.color[2]),pygame.Rect(block.x,block.y,block.width,block.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.food.color[0],self.model.food.color[1],self.model.food.color[2]),pygame.Rect(self.model.food.x,self.model.food.y,self.model.food.width,self.model.food.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.head.color[0],self.model.head.color[1],self.model.head.color[2]),pygame.Rect(self.model.head.x,self.model.head.y,self.model.head.width,self.model.head.height))
        pygame.draw.rect(self.screen, pygame.Color(self.model.head2.color[0],self.model.head2.color[1],self.model.head2.color[2]),pygame.Rect(self.model.head2.x,self.model.head2.y,self.model.head2.width,self.model.head2.height))
        for tail in self.model.tails:
            pygame.draw.rect(self.screen, pygame.Color(tail.color[0],tail.color[1],tail.color[2]),pygame.Rect(tail.x,tail.y,tail.width,tail.height))
        for tail in self.model.tails2:
            pygame.draw.rect(self.screen, pygame.Color(tail.color[0],tail.color[1],tail.color[2]),pygame.Rect(tail.x,tail.y,tail.width,tail.height))

class PyGameController:
    def __init__(self,model):
        self.model = model
        self.pause=True
        size = (640,480)
        screen = pygame.display.set_mode(size)
        view = PyGameWindowView(model,screen)
      
        
    def handle_keyboard_event(self,event):
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_LEFT:
            if self.model.head.vx==10.0:
                return
            else:
      		self.model.head.vx = -10.0
      		self.model.head.vy = 0.0
        if event.key == pygame.K_RIGHT:
            if self.model.head.vx==-10.0:
                return
            else:
      		self.model.head.vx = 10.0
      		self.model.head.vy = 0.0
        if event.key == pygame.K_UP:
            if self.model.head.vy==10.0:
                return
            else:
      		self.model.head.vx = 0.0
      		self.model.head.vy = -10.0
        if event.key == pygame.K_DOWN:
            if self.model.head.vy==-10.0:
                return
            else:
      		self.model.head.vx = 0.0
      		self.model.head.vy = 10.0
        
        if event.key == pygame.K_a:
             if self.model.head2.vx==10.0:
                 return
             else:
      		self.model.head2.vx = -10.0
      		self.model.head2.vy = 0.0
        if event.key == pygame.K_d:
            if self.model.head2.vx==-10.0:
                return
            else:
      		self.model.head2.vx = 10.0
      		self.model.head2.vy = 0.0
        if event.key == pygame.K_w:
            if self.model.head2.vy==10.0:
                return
            else:
      		self.model.head2.vx = 0.0
      		self.model.head2.vy = -10.0
        if event.key == pygame.K_s:
            if self.model.head2.vy==-10.0:
                return
            else:
      		self.model.head2.vx = 0.0
      		self.model.head2.vy = 10.0
        
        if event.key == pygame.K_RETURN:
            self.pause=False
            self.model.reset()
            view.draw()
      
      
if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    model = SnakeWorld()
    view = PyGameWindowView(model,screen)
    controller = PyGameController(model)  
    view.draw()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
               running = False
            if event.type == KEYDOWN:
                controller.handle_keyboard_event(event)
        
        view.draw()
        model.update() 
        time.sleep(.1)
        pygame.display.flip()
        if model.flag == True:
            screen.blit(model.msgObject,model.msgRect)
            screen.blit(model.msgObject2,model.msgRect2)
            screen.blit(model.msgObject25,model.msgRect25)
            screen.blit(model.msgObject255,model.msgRect255)
            screen.blit(model.msgObject3,model.msgRect3)
            pygame.display.flip()
            controller.pause=True
            while controller.pause:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                        controller.pause = False
                    if event.type == KEYDOWN:
                        controller.handle_keyboard_event(event)
                        pygame.display.flip()
                        model.flag = False
                    
    pygame.quit()
    
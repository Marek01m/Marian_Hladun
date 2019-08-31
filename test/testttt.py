#через деякий час invalid color argument

from random import randint
import pygame
pygame.init()
screen = pygame.display.set_mode((1200,600))
pygame.display.set_caption("My first game")
#clock = pygame.time.Clock()

x=50
y=50
width=40
height=60
vol=5


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x=x-vol
    if keys[pygame.K_RIGHT]:
        x=x+vol
    if keys[pygame.K_UP]:
        y=y-vol
    if keys[pygame.K_DOWN]:
        y=y+vol

    color=(randint(0,255),randint(0,255),randint(0,255))
    # color=([randint(0,256),randint(0,256),randint(0,256)])
    #without trace
    # screen.fill((0,0,0))          
    
    pygame.draw.rect(screen,color , [x, y, width, height], 5)
    pygame.display.update()
    clock.tick(60)



#не згладжуються лінії alines
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()
# WHITE=(255,255,255)
# done = False
# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    
    
#     #pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
#     pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
#     pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
#     #aaline згладжена лінія, товщина в цьому
#     # випадку не задається
#     pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
   
#     pygame.display.update()

#######################################################################################


# class Animal:
#     def __init__(self,type_a,sound,color):
#         self.t=type_a
#         self.s=sound
#         self.c=color
    
#     def animal_info(self):
#         print("Animal type is {}, its sound is {}, its color is {}".format(self.t,self.s,self.c))

# an=Animal("cow","mooo","black n white")

# an.animal_info()
# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("My first game")
# #clock = pygame.time.Clock()

# x=50
# y=50
# width=40
# height=60
# vol=20


# run = True
# clock = pygame.time.Clock()

# while run:
#     pygame.time.delay(100)
    
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             run=False

#     keys=pygame.key.get_pressed()
    
#     if keys[pygame.K_LEFT] and x>vol:
#         x=x-vol 
#     if keys[pygame.K_RIGHT] and x<500-width-vol:
#         x=x+vol
#     if keys[pygame.K_UP] and y>vol:
#         y=y-vol
#     if keys[pygame.K_DOWN] and y<500-height-vol:
#         y=y+vol


#     #without trace ##**
#     screen.fill((0,0,0))          
    
#     pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
#     pygame.display.update()
#   #clock.tick(60)


# import pygame

# # Define some colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Call this function so the Pygame library can initialize itself
# pygame.init()
 
# # Create an 800x600 sized screen
# screen = pygame.display.set_mode([800, 600])
 
# # This sets the name of the window
# pygame.display.set_caption('Fly')
 
# clock = pygame.time.Clock()

# #обновляємо екран 
# pygame.display.update()
 
# # Set positions of graphics
# background_position = [0, 0]
 
# # Load and set up graphics.
# #background_image = pygame.image.load("saturn_family1.jpg").convert()
# player_image = pygame.image.load("D:\Lectures\My_lect_Python\Game\+\player.png").convert()

# #Якщо в зображення не має прозорого слою, то щоб його встановити,
# #необхідно використати метод set_colorkey() класу Surface:
# player_image.set_colorkey(BLACK)
 
# done = False
 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True            
 
    
# # Get the current mouse position. This returns the position
#     # as a list of two numbers.
# #повертає поточну позицію мишки на екрані
#     player_position = pygame.mouse.get_pos()
#     x = player_position[0]
#     y = player_position[1]
 
#     # Copy image to screen:
# #копіює картинку на екран
#     screen.blit(player_image, [x, y])
 
# #обновляємо екран
#     pygame.display.flip()
 
#     clock.tick(60)


# pygame.quit()

import pygame
 
FPS = 60
W = 700  # ширина екрана
H = 300  # висота екрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координати і радіус круга
x = W // 2
y = H // 2
r = 50
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
 
    clock.tick(FPS)

    
import pygame
 
FPS = 60
W = 700  # ширина екрана
H = 300  # висота екрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координати і радіус круга
x = W // 2
y = H // 2
r = 50
 
motion = STOP
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = STOP
 
    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
 
    clock.tick(FPS)
#########################################################################
#PyGame#Оранжеве вікно

# import pygame

# pygame.init()

# WHITE = (255, 255, 255)  
# ORANGE = (255, 150, 100)

# DISPLAY_WIDTH = 400 
# DISPLAY_HEIGH = 400 

# gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

# pygame.display.set_caption("My first game")

# clock=pygame.time.Clock()

# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# # -------- Main Program Loop -----------
# while not done:
#   # --- Main event loop
#   for event in pygame.event.get(): # User did something
#     if event.type == pygame.QUIT: # If user clicked close
#         done = True # Flag that we are done so we exit this loop
  
#   # --- Game logic should go here
#   # --- Drawing code should go here
#   # First, clear the screen to white. Don't put other 
#   # drawing commands above this, 
#   # or they will be erased with this command.
  
#   gameDisplay.fill(ORANGE)
  
#   # --- Go ahead and update the screen with what we've drawn.
#   pygame.display.update()
  
#   # --- Limit to 60 frames per second
#   clock.tick(60)

#########################################################################
#PyGame#Event printing

# import pygame

# pygame.init()

# WHITE = (255, 255, 255)  
# ORANGE = (255, 150, 100)

# DISPLAY_WIDTH = 400 
# DISPLAY_HEIGH = 400 

# gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

# pygame.display.set_caption("My first game")

# clock=pygame.time.Clock()

# done = False

# clock = pygame.time.Clock()

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             # done=True    
#             print("User asked to quit.")
#         elif event.type == pygame.KEYDOWN:
#             print("User pressed a key.")
#         elif event.type == pygame.KEYUP:
#             print("User let go of a key.")
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("User pressed a mouse button")
  
#     gameDisplay.fill(ORANGE)
  
#     pygame.display.update()
  
#     clock.tick(60)

#########################################################################
#PyGame#

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()
# WHITE=(255,255,255)
# BLACK=(0,0,0)
# GRAY=(125,125,125)
# LIGHT_BLUE=(64,128,255)
# GREEN=(0,200,64)
# YELLOW=(225,225,0)
# PINK=(230,50,230)
# PI=3.14
# done = False

# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
    
    #############################################################
    
    #pygame.draw.rect(screen,WHITE,(20,20,100,75))
    #pygame.draw.rect(screen,(64,128,255),(150,20,100,75),8)


    # r1=pygame.Rect((150,20,100,75))

    # pygame.draw.rect(screen,WHITE,(20,20,100,75))
    # pygame.draw.rect(screen,YELLOW,r1)

    #############################################################

    # pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
    # pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
    #aaline згладжена лінія, товщина в цьому випадку не задається

    # pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
    
    #############################################################

    # pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
    # pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
    # pygame.draw.aalines(screen, WHITE, True, [[250, 210], [280, 250], [190, 290], [130, 230]])
    # pygame.draw.lines(screen, WHITE, True, [[450, 210], [480, 250], [390, 290], [330, 230]])

    #############################################################

    # передається прямокутна область, в якій промальовується еліпс
    # pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100), 5)

    # pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100))

    #############################################################

    # pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
    # pygame.draw.circle(screen, PINK, (300, 100), 70)

    #############################################################

    # pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    # pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)

    #############################################################

    # pygame.display.update()
    # clock.tick(60)

#########################################################################
#PyGame#

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()

# x=50
# y=50
# width=40
# height=60
# vol=5

# done = False

# while not done:
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
            
#     keys=pygame.key.get_pressed()

#     if keys[pygame.K_LEFT]:
#         x=x-vol
#     if keys[pygame.K_RIGHT]:
#         x=x+vol
#     if keys[pygame.K_UP]:
#         y=y-vol
#     if keys[pygame.K_DOWN]:
#         y=y+vol    
    
    
#     # pygame.draw.rect(screen, (255,0,0), [x, y, width, height],10)    
#     pygame.draw.rect(screen,(255,0,0), [x, y, width, height],5)    
#     screen.fill((0,0,0))

#     pygame.display.update()
#     clock.tick(60)


#########################################################################
#PyGame#rectangle moving with borders

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("Draw primitives")
# clock = pygame.time.Clock()

# x=50
# y=50
# width=40
# height=60
# vol=15

# done = False

# while not done:
#     pygame.time.delay(100)
    
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             done=True
            
#     keys=pygame.key.get_pressed()

#     if keys[pygame.K_LEFT] and x>vol:#>0
#         x=x-vol
#     if keys[pygame.K_RIGHT] and x<500-width-vol:
#         x=x+vol
#     if keys[pygame.K_UP] and y>vol:#>0
#         y=y-vol
#     if keys[pygame.K_DOWN] and y<500-height-vol:
#         y=y+vol    

#     #without trace
#     screen.fill((0,0,0))              
    
#     pygame.draw.rect(screen, (255,0,0), [x, y, width, height],10)    
     
#     pygame.display.update()
#     clock.tick(60)

#########################################################################
#PyGame#Homework image moving without tracing

import pygame
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
 
gameDisplay = pygame.display.set_mode([800, 600])
pygame.display.set_caption('hw1')
 
clock = pygame.time.Clock()

pygame.display.update()
background_position = [0, 0]
 
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load(r"C:\Users\Admin\Desktop\Marian_Hladun\Lesson 8\alien.png").convert()

player_image.set_colorkey(WHITE)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    # Get the current mouse position. This returns the position as a list of two numbers.
    #повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
  
    gameDisplay.blit(player_image, [x, y])
    pygame.display.update()
    gameDisplay.fill(BLACK)
    clock.tick(60)


pygame.quit()


#########################################################################
#PyGame#

# import pygame
 
# FPS = 60
# W = 700  # ширина екрана
# H = 300  # висота екрана
# WHITE = (255, 255, 255)
# BLUE = (0, 70, 225)
 
# pygame.init()
# sc = pygame.display.set_mode((W, H))
# clock = pygame.time.Clock()
 
# # координати і радіус круга
# x = W // 2
# y = H // 2
# r = 50
 
# while 1:
#     sc.fill(WHITE)
 
#     pygame.draw.circle(sc, BLUE, (x, y), r)
 
#     pygame.display.update()
 
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             exit()
#         elif i.type == pygame.KEYDOWN:
#             if i.key == pygame.K_LEFT:
#                 x -= 15
#             elif i.key == pygame.K_RIGHT:
#                 x += 15
 
#     clock.tick(FPS)

#########################################################################
#PyGame#

# import pygame
 
# FPS = 60
# W = 700  # ширина екрана
# H = 300  # висота екрана
# WHITE = (255, 255, 255)
# BLUE = (0, 70, 225)
# RIGHT = "to the right"
# LEFT = "to the left"
# STOP = "stop"
 
# pygame.init()
# sc = pygame.display.set_mode((W, H))
# clock = pygame.time.Clock()
 
# # координати і радіус круга
# x = W // 2
# y = H // 2
# r = 50
 
# motion = STOP
 
# while 1:
#     sc.fill(WHITE)
 
#     pygame.draw.circle(sc, BLUE, (x, y), r)
 
#     pygame.display.update()
 
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             exit()
#         elif i.type == pygame.KEYDOWN:
#             if i.key == pygame.K_LEFT:
#                 motion = LEFT
#             elif i.key == pygame.K_RIGHT:
#                 motion = RIGHT
#         elif i.type == pygame.KEYUP:
#             if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#                 motion = STOP
 
#     if motion == LEFT:
#         x -= 15
#     elif motion == RIGHT:
#         x += 15
 
#     clock.tick(FPS)

#########################################################################
#PyGame#Homework Ball moving from left to right stopless

import pygame
 
FPS = 60
W_H = [800,300]
WHITE = (255, 255, 255)
BLUE = (120, 150, 200)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
 
pygame.init()
gameDisplay = pygame.display.set_mode(W_H)
pygame.display.set_caption('Ball movin`')
clock = pygame.time.Clock()
x = W_H[0] // 2
y = W_H[1] // 2
r = 50
 
motion = STOP
 
while 1:
    gameDisplay.fill(WHITE)
 
    pygame.draw.circle(gameDisplay, BLUE, (x, y), r)
 
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
    if x-r > W_H[0]:
        x = -r
    elif x+r < 0:
        x = W_H[0] + r
    if motion == LEFT:
        x -= 5
    elif motion == RIGHT:
        x += 5
    
 
    clock.tick(FPS)

#########################################################################
#PyGame#

# import pygame
# pygame.init()
# gameDisplay=pygame.display.set_mode((400,300))
# pygame.display.set_caption("My first game")
# clock=pygame.time.Clock()
# crashed=False
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("User asked to quit.")
#         elif event.type == pygame.KEYDOWN:
#             print("User pressed a key.")
#         elif event.type == pygame.KEYUP:
#             print("User let go of a key.")
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             print("User pressed a mouse button")

        
#     pygame.display.update()

#     clock.tick(60)

# pygame.quit()
#quit()

#########################################################################
#PyGame#

# import pygame

# pygame.init()

# gameDisplay=pygame.display.set_mode((400,300))

# pygame.display.set_caption("my first game")

# clock=pygame.time.Clock()

# crashed=False
# while not crashed:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             crashed = True

#         print(event)

#     pygame.display.update()

#     clock.tick(60)

# pygame.quit()
# #quit()

#########################################################################
#tkinter_1#

# tkinter бібліотека для розробки графічного інтерфейсу

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна

# root.title("Сaught the BALL")

# #створ. об'єкт класу canvas

# canv = Canvas(root,bg='white')

# #pack пакувальник, який дозволяє розміщати 
# #зображення одне за одним
# #fill=BOTH дозволяє заповнювати все доступне місце і по ширині і по висоті
# # expand=1 при розширенні вікна мітка завжди буде посередині 

# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# ###################################################
# def new_ball():
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
    
#     #(x-r,y-r)-координати верхнього лівого кута
#     #(x+r,y+r)- координати нижнього правого кута
#     #квадрата, в якому промальовується коло

#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    
#     #root.after(1000,new_ball) 
#     # через 1000 мілісек викон.
#     # функцію  new_ball()
    
#     root.after(1000,new_ball)
# #######################################################     

# new_ball()
# mainloop()

#########################################################################
#tkinter_2#

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# ######################################################
# def new_ball():
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
# ######################################################### 

#  #додали обробку події click
#  #     

# def click(event):
#     print('click the button')   
     
# #############################################

# new_ball()

# #canv.bind зв'язує між собою декілька подій

# canv.bind('<Button-1>', click)
# mainloop()

# #########################################################################
# #tkinter_3#

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# #використання global не найкраща ідея
# #краще використовувати ООП
# #global означає, що змінні будуть 
# #вважатися глобальними, і їх 
# # значення збережеться і після 
# # завершення роботи функції, а не буде
# # знищене як це станеться з усіма локальними 
# # змінними після завершення виконання функції

# #################################################3
# def new_ball():
#     global x,y,r
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
# #######################################################
     
#  #щоб визначити, чи попали ми в круг,
#  # необхідно знати його координати, 
#  # радіус круга і координати мишки в момент кліку.
#  # Координати мишки легко отримати через 
#  # event.x, event.y.    
# def click(event):
#     print(x,y,r)    
     


# new_ball()
# canv.bind('<Button-1>', click)
# mainloop()


# #########################################################################
# #tkinter_4#

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# ############################################################
# def new_ball():
#     global x,y,r
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     #canv.create_text(20,20,text=str(points), font = 'Arial 20')
    
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
# ###################################################################

#  # функція, яка провіряє, чи не лежить 
#  # точка event.x,event.y дальше, ніж r 
#  # від точки x,y. Для цього, з допомогою
#  # теореми Піфагора ми знаходимо
#  # відстань між двома точками і порівнюємо 
#  # з радіусом круга.
#  #  
#  # якщо відстань(гіпотенуза) більша за радіус 
#  # круга, то клік відбувся зовні круга
#  #  
#  # якщо відстань(гіпотенуза) менша за радіус 
#  # круга, то клік відбувся всередині круга    
     
# def click(event):
#     global points
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1 #змінна підрахунку кількості співпадінь (вгадувань)
 
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)
 
# mainloop()

# #########################################################################
# #tkinter_5#

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# def new_ball():
#     global x,y,r
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     #виводити рахунок в консоль незручно
#     #зручніше його вивести на canvas
#     #використавши функцію canv.create_text()
#     canv.create_text(60,20,text="Score: "+str(points), font = 'Arial 20')
    
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
     
     
# def click(event):
#     global points
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1
 
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)
 
# mainloop()

# #########################################################################
# #tkinter_6#

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# def new_ball():
#     global x,y,r,ball
#     canv.delete(ball)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
         
# def click(event):
#     global points, x, text
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1
#         x = -1000
# #видалення круга при кліку
#         canv.delete(text)
#         canv.delete(ball)
#         text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')

        
# #щоб не можна було «накручувати» очки, 
# # клікаючи багато разів по кругу, 
# # поки він не зникне

# #Після кліку круг не зникає і це не ok.
# #Можна видалити все 
# # canv.delete(ALL), 
# # але тоді буде видалятись і рахунок

# #краще дати імена всім графічним примітивам
# # (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
# #щоб можна було видалити ball, треба перед викликом 
# #функції ball() намалювати цей ball
# ball = canv.create_oval(-100,0,0,0)
# text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)


# mainloop()

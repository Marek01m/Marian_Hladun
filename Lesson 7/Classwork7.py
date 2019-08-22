#########################################################################
#Weather API pyowm#

# import pyowm
# my_locate=input("Enter your locate: ")
# owm = pyowm.OWM('673017e269af3efe9b48a6ccbb21f937')

# observation = owm.weather_at_place(my_locate)
# w = observation.get_weather()  # <Weather - reference time=2013-12-18 09:20,status=Clouds>

# temperature=w.get_temperature('celsius')['temp']
# wind=w.get_wind()['speed'] # {'speed': 4.6, 'deg': 330}
# humidity=w.get_humidity() # 87
# detailed=w.get_detailed_status() # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# pressure = w.get_pressure()['press']
# time=observation.get_reception_time(timeformat='iso')[:19]         
# print("For {} temperature in {} is {}С°, in this city is {} , the speed of wind is {} mps , humidity is {}% , pressure is {}mm.".format(time,my_locate,temperature,detailed,wind,humidity,pressure))

#########################################################################
#Task1#

# from random import randint

# num=randint(1,101)
# #print(num)
# user_n=int(input("Enter ur num: "))
# checkbox_u=False
# while not checkbox_u:
#     if user_n==num:
#         print("You woN!Congtrats!")
#         checkbox_u=True
#     elif user_n<num:
#         user_n=int(input("Try bigger num (num<x): ")) 
#     else:
#         user_n=int(input("Try smaller num (num>x): "))       

#########################################################################
#Task2#

# import math

# def rectangle():
#     a = float(input("Input width: "))
#     b = float(input("Input height: "))
#     print("Square={}".format(a*b))
 
# def triangle():
#     a = float(input("Input basis: "))
#     h = float(input("Input height: "))
#     print("Square={}".format(0.5 * a * h))
 
# def circle():
#     r = float(input("Input radius: "))
#     print("Square={}".format(math.pi*pow(r, 2))

# figure = input("1-rectangle, 2-triangle, 3-circle: ")
# if figure == '1':
#   rectangle()
# elif figure == '2':
#   triangle()
# elif figure == '3':
#   circle()
# else:
#   print("Input error")
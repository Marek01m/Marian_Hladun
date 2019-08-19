# import pyowm
# my_locate=input("Введіть місто: ")
# owm = pyowm.OWM('673017e269af3efe9b48a6ccbb21f937')

# observation = owm.weather_at_place(my_locate)
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>


# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)



from random import randint

num=randint(1,11)
user_n=0

print(num)
user_n=input("Enter ur num(1-100): ")
if user_n==num:
    print("You win!")        
else:
            


# user_n=int(None)
# while not user_n==num:
#     user_n=input("Enter ur num: ") 
#########################################################################
#Task1#

# x=int(input("Яка довжина списку: "))
# nums=[int(input("enter num: ")) for i in range(x)]
# print("max--->{}, min--->{}".format(max(nums),min(nums)))

#########################################################################
#Task2#

# numlist=list(range(1,11))
# print(numlist)
# parni2=[]
# neparni3=[]
# ni2ni3=[]
# for i in numlist:
#     if i%2==0:
#         parni2.append(i)
#     elif i%3==0:
#         neparni3.append(i)
#     elif i%2>0 and i%3>0:
#         ni2ni3.append(i)
# print(parni2)
# print(neparni3)
# print(ni2ni3)

#########################################################################
#Task3#

# num = int(input("Enter a number: "))
# factorial = 1

# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers.")
# elif num == 0:
#    print("The factorial of the number 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of {0} is {1}".format(num,factorial))

#########################################################################
#Task4#

# login=input("Enter ur login: ")
# while not login=="First":
#     print("Incorrect")
#     login=input("Enter ur login: ")
# else:
#     print("Ви ввели вірно!")    

#########################################################################
#Task5# and #Task6#

# x=int(input("Яка довжина списку: "))
# nums=[int(input("enter num: ")) for i in range(x)]
# i=0
# while nums[i]>0:
#     print(nums[i], end="->")
#     i+=1
# else:
#     print("STOP! Zero or neg!")    

#########################################################################
#Task7#

# for number in range(10, 31):
#     if number > 1:
#         for i in range(2, number):
#             if number % i == 0:
#                 print(number, ' equals 2 * {}'.format(number/2))
#                 break
#         else:
#             print(number, 'is a prime number')

#########################################################################
#Task8#

# text="""Ти знаєш, що ти – людина?
# Ти знаєш про це чи ні?
# Усмішка твоя – єдина,
# Мука твоя – єдина,
# Очі твої – одні.

# Більше тебе не буде.
# Завтра на цій землі
# Інші ходитимуть люди,
# Інші кохатимуть люди –
# Добрі, ласкаві й злі."""

# s_text = [el for el in sorted(text.split(),key=len)]
# print(s_text)


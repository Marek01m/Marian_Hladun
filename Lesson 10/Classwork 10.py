#Task1#

# class NegNumError:
#     pass
# try:
#     num=int(input("Введіть ціле число "))
#     if num%2==0:
#         print(num,"-ПАРНЕ")
#     elif num<0:
#         raise NegNumError("Only positive num")   
#     else:
#         print(num,"-НЕПАРНЕ")
       
# except ValueError:
#     print("error!Only integer!")
# except NegNumError:
#     print("Only pos num")

#____________________________________________________________________

# n = input("Input entire number: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("\n You entered incorrect data!\n")
#         n = input("Input entire number:\n ")
 
# if n % 2 == 0:
#     print("{0} is the even number.".format(n))
# else:
#     print("{0} is the odd number.".format(n))

#Task2#

# class NegNumError(Exception): 
#     def __init__(self, data): 
#         self.data = data
#     def __str__(self):
#         return repr(self.data)


# while 1:
#     try:
#         age=int(input("Введіть ваш вік : "))
#         if age<0:
#             raise NegNumError("Enter positive number!")
#         elif age%2==0:
#             print("Ваш вік є парним числом--->",age) 
#         else:
#             print:("Ваш вік є непарним числом--->",age)  
#     except NegNumError as e:
#         print("Here is error!\n",e.data)            
#     except ValueError:
#         print("\n You entered incorrect data!\n")
        
#________________________________________________________________________________________________

# def enterage(age):
#     if age<0:
#         raise ValueError("Only positive integers are allowed!")
    
#     if age%2==0:
#         print("age is even")
#     else:
#         print("age is odd")

# try:
#     num=int(input("Enter your age: "))
#     enterage(num)

# except ValueError as e:
#     print("Only positive integers are allowed!!!",e)  



#Task3

# try:
#      num1,num2=eval(input("Enter two numbers,separated by a coma: "))
#      result: num1/num2
#      print("Result is", result)

# except ZeroDivisionError:
#     print("Division by zero is error!")
# except ValueError:
#     print("ValueError.")
# except SyntaxError:
#     print("Comma is missing. Enter numbers separated by the coma like this 1,2")
# except:
#     print("Wrong input") 
# 

#Task 4

# d={
# 1:"Monday",
# 2:"Tuesday",
# 3:"Wednesday",
# 4:"Thursday",
# 5:"Friday",
# 6:"Saturday",
# 7:"Sunday"
# }
# while True:
#     try:
#         i=int(input("Enter the day of the week: "))
#     except ValueError:
#         print("You did not enter a number!")
#     else:
#         print(d.get(i, "There is no such day of the week!"))

#__________________________________________________________________

#day_list=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# try:
#     num=int(input("Enter number from 1 to 7: "))
#     if num <=0 or num>7:
#         raise IndexError("Youre number is ut of range")
#         print(day_list[num-1])
# except ValueError:
#     print("Wrog Input!")


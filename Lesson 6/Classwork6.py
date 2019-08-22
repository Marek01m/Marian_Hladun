#########################################################################
#Task1#

# def do_ser_ar(*args):
#     x=0
#     ser=0
#     for i in args:
#         ser=i+x/len(args)
#     return  ser   

#def arithmetic_mean(*args):
#     """ This function calculates the arithmetic mean of a non-empty
#         arbitrary number of numerical values """
#     return sum(args) / len(args)

#print(do_ser_ar(2,2,2))

#print(arithmetic_mean(45,32,89,78))
# print(arithmetic_mean(8989.8,78787.78,3453,78778.73))
# print(arithmetic_mean(45,32))
# print(arithmetic_mean(45))
# print(arithmetic_mean.doc)

#########################################################################
#Task 2#

# def module(num):
#     if num >= 0:
#         return num
#     else 
#         return -num    


# def do_module(x):
# if x>=0:
#     return x
# else:
#     return str(x)[1:]   

# print(do_module(-5))

#########################################################################
#Task 3#

# def max_from2 (a,b):
#     """This func returns max number from two"""
#     a=int(a)
#     b=int(b)
#     if a>b:
#         return "a is max"
#     elif a==b:
#         return "a=b"
#     else:
#         return "b is max"    

# print(max_from2(5,7))        

#########################################################################
#Task 4#

# def sq_rectangle(l,h):  
#     return l*h

# def sq_triangle(a,h,f=0.5):
#     return a*h*f

# def sq_circle(r,PI=3.14):
#     return r**2    

# choice=input("Choose 1-rectangle, 2-triangle, 3-circle: ")
# if choice=='1':
#     length=input("a: ")
#     height=input("b: ")
#     print(sq_rectangle(length,height))
# elif choice=='2':
#     storona=input("c: ")
#     height=input("h(c): ")
#     print(sq_straight_triangle(storona,height))
# elif choice=="3":
#     radius=input("r: ")
#     print(sq_circle(radius))
# else:
#    print("Input Error")


# def rectangle():
#     a = float(input("Input width: "))
#     b = float(input("Input height: "))
#     print("Square={}".format(a*b))
 
# def triangle():
#     a = float(input("Input basis: "))
#     h = float(input("Input height: "))
#     print("Area={}".format(0.5 * a * h))
 
# def circle():
#     PI=3.14
#     r = float(input("Input radius: "))
#     print("Square={}".format(PI * r**2))

# figure = input("1-rectangle, 2-triangle, 3-circle: ")
# if figure == '1':
#   rectangle()
# elif figure == '2':
#   triangle()
# elif figure == '3':
#   circle()
# else:
#   print("Input error")

########################################################################
# Task 5#

# def do_sum(x):
#     sum=0
#     for i in x:
#         sum+=int(i)
#     return sum  

# print(do_sum('678'))    

#########################################################################     
#Task 6#                           

# from decimal import Decimal

# def sum(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def multi(a,b):
#     return a*b

# def dev(a,b):
#     if b==0:
#         return print("Cannot devide by zero")
#     else:
#         return a/b

# def calc():
#     running=input("Запустити калькулятор? Y/N ").lower()
#     while running=='y':

#        choice=input("Виберіть дію: + - * /: ")
#        first_num=Decimal(input("Введіть переше число: "))
#        second_num=Decimal(input("Введіть друге число: "))

#         if choice=="+":
#             print("{0}{2}{1}={3}".format(first_num,second_num,choice,sum(first_num,second_num)))
#             running=input("Бажаєте продовжити? Y/N ").lower()
#         elif choice=="-":
#             print("{0}{2}{1}={3}".format(first_num,second_num,choice,sub(first_num,second_num)))
#             running=input("Бажаєте продовжити? Y/N ").lower()
#         elif choice=="*":
#             print("{0}{2}{1}={3}".format(first_num,second_num,choice,multi(first_num,second_num)))
#             running=input("Бажаєте продовжити? Y/N ").lower()    
#         elif choice=="/":
#             print("{0}{2}{1}={3}".format(first_num,second_num,choice,dev(first_num,second_num)))
#             running=input("Бажаєте продовжити? Y/N ").lower()
#         else:
#             print("Choose correct symbol!")
#             running=input("Бажаєте продовжити? Y/N ").lower()
#     else:
#        print("Thank you for choosing our product!")


# calc()

#########################################################################
#Task 7#
def fib_r(n):  
    return n if n<=1 else (fib_r(n-1)+fib_r(n-2))
   
quantity_of_fibs = int(input("How many fibonacci? "))  

if quantity_of_fibs <= 0:  
   print("Plese enter a positive integer", end=" ")  
else:  
   print("Fibonacci sequence:",end=" ")
   fib_list=[fib_r(i) for i in range(quantity_of_fibs)]
   print(fib_list)  
   
   
# for i in range(quantity_of_fibs):  
#    print(fib_r(i))  


#########################################################################
#Task 8#

# def d(a,b,c):
#     return b**2-4*a*c

#########################################################################
#*END*#
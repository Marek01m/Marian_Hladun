#Task1

# def do_ser_ar(*args):
#     x=0
#     ser=0
#     for i in args:
#         ser=i+x/len(args)
#     return  ser   

#print(do_ser_ar.__doc_)
# print(ser_ar(2,2,2))

##############################################
#Task 2
# def module(x):
#     if num >= 0:
#         return numb
#     else 
#         return -num    



# def do_module(x):
# if x>=0:
#     return x
# else:
#     return str(x)[1:]
#     

# print(do_module(-5))

#####################
#Task 3

# def max_from2 (a,b):
#     """This func returns max number from two"""
# a=int(a)
# b=int(b)
#     if a>b:
#         return "a is max"
#     elif a==b:
#         return "a=b"
#     else:
#         return "b is max"    

# print(max_from2(5,7))        

####################
#Task 4


# def sq_rectangle(l,h):  #дописати 1\2 на основу і пл прям
#     return l*h

# def sq_straight_triangle(a,h,f=0.5):
#     return a*h*f

# def sq_circle(r,PI=3.14):
#     return r**2    

# choice=input("Choose 1-rectangle, 2-stright triangle, 3-circle")
# if choice=='1':
#     length=input("Length: ")
#     height=input("Height: ")
#     print(sq_rectangle(length,height))
# elif choice=='2':
#     katet=input("katet: ")
#     height=input("Height: ")
#     print(sq_straight_triangle(katet,height))
# elif choice=="3":
#     radius=input("Radius: ")
#     print(sq_circle(radius))
# else:
#    print("Input Error")

####################
#Task 5


# def do_sum(x):
#     sum=0
#     for i in x:
#         sum+=int(i)
#     return sum  

# print(do_sum('678'))    



########################            #константа python
#Task 6                           

def calculator():
    a=input("Enter ur number1: ")
    symb=input("Enter act symb: ")
    b=input("Enter ur number2: ")
    a=int(a)
    b=int(b)
    symb=str(symb)
    def plus(a,b):
        return a+b
    def minus(a,b):
        return a-b
    def zirochka(a,b):
        return a*b
    def slash(a,b):
        return a/b   
    if symb=="+":
        print(plus(a,b))

        
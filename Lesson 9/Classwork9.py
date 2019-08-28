# class A:    pass
# def myMethod (self, x):    return x * x
# A.m1 = myMethod
# A.attr1 = 2 * 2


class Animal:
    def __init__(self,type_a,sound,color):
        self.t=type_a
        self.s=sound
        self.c=color
    
    def animal_info(self):
        print("Animal type is {}, its sound is {}, its color is {}".format(self.t,self.s,self.c))

an=Animal("cow","mooo","black n white")

an.animal_info()


# class Figure:
#     def __init__(self,color):
#         self.c=color
    
#     def get_color(self):
#         print self.c

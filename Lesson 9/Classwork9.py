class Animal:
    def __init__(self, spec="None", leg=0):
        self.spec=spec
        self.leg=leg
    def name(self):
        print("Im a "+ self.spec)
    def walk(self):
        print("I can walk!")
    
class Rabbit(Animal):
    def __init__(self):
        super().__init__("rabbit",4)
    
class Ostrich(Animal):
    def __init__(self):
        super().__init__("ostrich", 2)

r=Rabbit()
r.name()
r.walk()

o=Ostrich()
o.name()
o.walk()

##################################################################################################################

class Figure:
    def __init__(self,figure_color):
        self.color=figure_color
                
    def get_color(self):
        print(f"Figure color is {self.color}")

class Rectangle(Figure):
    def __init__(self, height, width):
        super().__init__("yellow")
        self.h=height
        self.w=width
            
    def square(self):
        return self.h*self.w

    def info(self):
        print(f"Rectangle color is {self.color}, height={self.h}, width={self.w}")

class Square(Figure):
    def __init__(self, side):
        super().__init__("orange")
        self.s=side
              
    def square(self):
        return self.s**2

    def info(self):
        print(f"Square color is {self.color}, side={self.s}")    

r=Rectangle(4,8)
r.info()
print(f"Area is {r.square()}") 

sq=Square(5)
sq.info()
print(f"Area is {sq.square()}")            

class Point:
     def __init__(self, x, y):   #initialize object. The object starts working the moment it is created and gives the object the x,y properties.
          self.x = x
          self.y = y

     def move(self):
          print("move")

     def draw(self):
          print("draw")


point = Point(10, 20)
point.x = 11

print(point.x)

######### Excercise #########

class Person:
     def __init__(self, name):
          self.name = name 

     def talk(self):
          print(f"Hi, I am {self.name}")

john = Person("John")
john.talk()

bob = Person("Bob")
bob.talk()

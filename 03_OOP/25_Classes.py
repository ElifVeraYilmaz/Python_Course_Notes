'''Conventions are the 'unwritten rules' of clean code. 
   They aren't technical requirements, but they are professional necessities. '''

class Point: #Pascal Case ex: EmailClient
     def move(self):
          print("move")

     def draw(self):
          print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)

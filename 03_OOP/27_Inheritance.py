'''Duplicate code leads to a 'maintenance nightmare' 
because a single bug needs to be fixed in multiple places.
          So Dont repeat yourself !!!'''
class Mammal:
     def walk(self):
          print("walk")


class Dog(Mammal):
     def bark(self):
          print("bark")

    
class Cat(Mammal):
     pass # Python doesn't like empty classes, so we wrote a pass here if we dont wanna write anything.

dog1= Dog()
dog1.bark()
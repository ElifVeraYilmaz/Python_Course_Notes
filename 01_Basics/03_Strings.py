first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder.'
msg = f'{first} [{last}] is a coder.' # It is called formatted string. Curly brackets act as placeholders.
print(message)
print(msg)

##############

## 'len' for character count
course = 'Python for Beginners'
print(len(course))  # len and print are general purpose functions, they dont belong to strings or numbers or other kind of objects. 
print(course.upper()) # upper method needs string object. This is what sets functions and methods apart.
print(course) # The method didn't modify the variable.
print(course.find('P')) # It finds which index it is at.
print(course.replace('Beginners', 'Absolute Beginners')) #It is case sensitive otherwise it won't find the word.
print('Python' in course) #Boolean value expression.True or False 


#### Note: Strings in Python are immutable. Methods like .upper() return a new string rather than modifying the original one.





print(10 / 3) # The result is a floating point number.
print(10 // 3) #The result is a integer number.
print(10 % 3) # The result is remainder of devision.
print(10 ** 3) # 10 to the power of 3. 

######## Augmented Assignment Operator ##########

x = 10
x = x + 3
x += 3 # += this is augmented assignment operator or enhanced the assignment operator.
print(x)

######## Operator Priority ##########

x = 10 + 3 * 2 
print(x) # Priority is the same as in math.

################

x = 2.9
print(round(x)) #It rounds the number to an integer.
print(abs(-1.8)) #It takes the absolute value.


######## Modules ##########

'''A module is simply a file containing Python code (functions, classes, or variables). 
We use modules to break down large programs into smaller, manageable, and organized files.

Option A: import module_name
Ex: import converters
    print(converters.kg_to_lbs(70))

Option B: from module_name import function_name
Ex: from converters import kg_to_lbs
    print(kg_to_lbs(70))  

    
!!!!Important Warning: Never name your personal files after built-in Python modules (e.g., do not name your file math.py, random.py, or os.py) '''

import math 

print(math.ceil(2.9)) # Rounds up to the nearest integer.
print(math.floor(2.9)) # Rounds down to the nearest integer.


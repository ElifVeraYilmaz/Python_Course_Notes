name = input('What is your name? ') #Prints output to the terminal. We stored the given answer as a variable called 'name'.
print(' Hi ' + name)


# birth_year = input('Birth year: ')
# age = 2026 - birth_year
# print (age)

## Because it recognizes the birth_year as a string, it cannot subtract it from the number and will give an error.

birth_year = input('Birth year: ')
age = 2026 - int(birth_year)
print (age)

print(type(age))
print(type(birth_year))

## Everything entered into the input field is always considered a string, so you need to convert it to an integer or float.


course = "Python for Beginners"
print(course[0]) # [0] means first character. [-1] means last character. -> s
print(course[0:3]) # It prints characters from 0 to 3. 3 is not included.
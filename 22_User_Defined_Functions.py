''' If you use the same 5 line code in 10 different places in the project,
    you'll need to fix it in all 10 places when an error occurs.
    But if you define functions, you only need to fix that function. '''

#The location we define is important. We cannot call it without defining it !!

def greet_user(name, surname):   # Define
     print(f'Hi {name} {surname}!')
     print('Welcome aboard')  

print("Start")
greet_user("John", "Smith") # We must write the parameters in the parentheses; otherwise, it will throw an error.
print("Finish")
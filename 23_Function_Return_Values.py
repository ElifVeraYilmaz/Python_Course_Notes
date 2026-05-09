def square(number):
     return number * number 

# If we had used print(number * number) inside the function instead of return,
# the function would return 'None' by default. 
# Therefore, print(square(3)) would display the result followed by 'None'.

print(square(3))
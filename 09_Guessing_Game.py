secret_number = 4

# Replaced 'i' with 'guess_count' to improve code readability. 
# This makes the variable's purpose clear and follows 'Clean Code' principles.
guess_count = 0 
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: ")) # Since the input always takes a string, we converted it to an integer.
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
   print("Sorry you failed :(")
         
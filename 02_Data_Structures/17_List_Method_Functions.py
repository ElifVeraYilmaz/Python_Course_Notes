numbers = [5, 2, 1, 7, 4 , 5]
numbers2 = numbers.copy() # Creates a shallow copy of the list.
numbers.append(20) # I added a number to the list.
print(numbers)

numbers.insert(0, 10) # It will be added at the beginning of the list.
print(numbers)

numbers.remove(10) 
print(numbers)

numbers.pop() # Removes the last item from the list.
print(numbers)

print(numbers.index(5)) # 0
print (50 in numbers) # I asked about the existence of 50 on the list. (False)
print(numbers.count(5)) # There are two 5s in the list.

numbers.sort()
numbers.reverse()
print(numbers)

numbers.clear() 
print(numbers)

print(numbers2)





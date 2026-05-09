matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]
# matrix[0][1] = 20 # We can modify like this.
print(matrix[0][1]) # The second number of the first list will be printed.

for row in matrix:
     for item in row:
          print(item)
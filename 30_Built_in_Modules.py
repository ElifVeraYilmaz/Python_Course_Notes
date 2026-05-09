# seach 'Python 3 module ibdex' on google.

import random

for i in range(3):
  print(random.random()) # When we call it will give us random number 0 to 1
  print(random.randint(10, 20))


members = ['John', 'Mary']  
leader = random.choice(members)
print(leader)


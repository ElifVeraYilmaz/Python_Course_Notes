custumer = {
     "name" : "John Smith",
     "age" : 30,   # "age" : 40, (We cant define 2 same key.)
     "is_verified" : True
}
print(custumer ["name"])

print(custumer.get("birthdate" )) # None 
# print(custumer ["birthdate"]) # Key error.

print(custumer.get("birthdate", "Jan 1 1980" ))

######### Excersize ###########

phone = input("Phone: ")
digits_mapping = {
     "1": "One",
     "2": "Two",
     "3": "Three",
     "4": "Four"
}
output = ""
for ch in phone:
     output += digits_mapping.get(ch, "!") + " "
print(output)

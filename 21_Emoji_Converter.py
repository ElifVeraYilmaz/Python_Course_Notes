message = input("> ")
words = message.split(' ') # It allows us to separate words and write them in the form of a list.
emojis = {
     ":)": "😄",
     ":(" : "🙁"
}
output = ""
for word in words:
     output += emojis.get(word, word) + " "
print(output)
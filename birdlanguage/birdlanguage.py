import random
translate = input(str("Enter text to translate: "))
result = ""
for letter in translate:
    if letter in "aeiouy":
        result += letter * 2
    elif letter in "bcdfghjklmnpqrstvwxz":
        result += letter + random.choice("aeiouy")
    else:
        result += letter
print(result)
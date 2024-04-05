word = input()
uppercase = sum(map(str.isupper,word))
if len(word)/2 < uppercase:
    print(word.upper())
else:
    print(word.lower())

word = input().lower()
newword = ""
for x in word:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'y':
        newword += ""
    else:
        newword += "." + x
print(newword)
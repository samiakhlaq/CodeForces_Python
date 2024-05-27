def express(n,a,b):
    s = ''
    for x in range(n):
        if x%2 == 0:
            s+= a
        else:
            s+=b
    return s[:-5]+'it'
a = "I hate that "
b = "I love that "
n = int(input())
print(express(n,a,b))
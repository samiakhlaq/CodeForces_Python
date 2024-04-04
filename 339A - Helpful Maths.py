n1=n2=n3 = 0
calc = input()
for x in range(len(calc)):
    if calc[x] == '1':
        n1 = n1+1
    elif calc[x] == '2':
        n2 = n2+1
    elif calc[x] == '3':
        n3 = n3+1
result= "1+"*n1 + "2+"*n2 + "3+"*n3
print(result[:-1])
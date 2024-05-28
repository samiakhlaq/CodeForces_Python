test = int(input())
for x in range(test):
    str = input()
    if len(set(str)) == 1:
        print("NO")
    else:
        print('Yes')
        print(str[1:]+str[0])
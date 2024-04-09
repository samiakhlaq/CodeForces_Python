first_num = input()
seconde_num = input()
for x,y in zip(first_num,seconde_num):
    if x == y:
        print('0',end="")
    else:
        print('1',end="")

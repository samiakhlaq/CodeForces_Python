friends = int(input())
first_list = list(map(int,input().split()))
squence_list= ""
for x in range(friends):
    for i in range(friends):
        if first_list[i] == x+1:
            squence_list+= str(i+1) + " "
print(squence_list[:-1])
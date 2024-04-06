lenght = int(input())
result = input()
Anton=Danik = 0
for i in result:
    if i == 'D':
        Danik+=1
    else:
        Anton+=1
if Danik > Anton:
    print("Danik")
elif Anton > Danik:
    print("Anton")
else:
    print("Friendship")
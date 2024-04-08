room = int(input())
c=0
for _ in range(room):
    inside,capacity = map(int,input().split())
    if capacity-inside >= 2:
        c+=1
print(c)
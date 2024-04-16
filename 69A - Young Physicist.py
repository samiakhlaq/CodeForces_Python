num = int(input())
x=y=z=0
for i in range(num):
    vectors = list(map(int,input().split()))
    x+=vectors[0]
    y+=vectors[1]
    z+=vectors[2]
if (x,y,z) == (0,0,0):
    print("YES")
else:
    print("NO")
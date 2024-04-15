num_op = int(input())
c=0
for x in range(num_op):
    test = int(input())
    array = sorted(list(map(int,input().split())))
    if (test != 1):
        for y in range(1,test):
            if array[y]-array[y-1] >1:
                c+=1
                break
    if c == 0:
        print("YES")
    else:
        print("NO")
    c=0
    array = []
    
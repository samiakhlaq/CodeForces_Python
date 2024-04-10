num_op = int(input())
for x in range(num_op):
    numbers = list(map(int,input().split()))
    if numbers[0]<numbers[1]<numbers[2]:
        print("STAIR")
    elif numbers[0]<numbers[1]>numbers[2]:
        print("PEAK")
    else:
        print("NONE")
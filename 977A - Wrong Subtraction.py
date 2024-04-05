num,step = map(int, input().split())
for x in range(step):
    if num%10 == 0:
        num = num/10
    else:
        num = num-1
print(int(num))
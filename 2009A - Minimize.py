def solve(a,b):
    if a==b:
        print(0)
    else:
        print((1+(b-(a+1))))
test = int(input())
for x in range(test):
    a,b = map(int,input().split())
    solve(a,b) 
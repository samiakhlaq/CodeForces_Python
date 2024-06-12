def divisible(a,b):
    print((b-a%b)%b)

t = int(input())
for x in range(t):
    a,b = map(int,input().split())
    divisible(a,b)

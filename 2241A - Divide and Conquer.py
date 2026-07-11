def solve(x,y):
    if x%y == 0:
        print("YES")
    else:
        print("NO")
t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    solve(x,y)
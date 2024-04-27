test = int(input())
for x in range(test):
    n,c,d = map(int,input().split())
    elements = list(map(int,input().split()))
    first = min(elements)
    adjust = []
    adjust.append(first)
    for i in range(n-1):
        adjust.append(adjust[i]+d)
    for i in range(n):
        current = adjust[i]
        for j in range(1,n):
            current = current + c
            adjust.append(current)
    if sorted(elements) == sorted(adjust):
        print("YES")
    else:
        print("NO")
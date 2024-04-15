num_contest = int(input())
points = list(map(int,input().split()))
amazing = 0
for x in range(1,num_contest):
    if points[x]> max(points[:x]) or points[x]< min(points[:x]):
        amazing+=1
print(amazing)
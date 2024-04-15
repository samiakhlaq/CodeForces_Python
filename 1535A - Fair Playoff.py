test = int(input())
for x in range(test):
    skills = list(map(int,input().split()))
    fair = sum(sorted(skills)[2:])
    given = max(skills[:2]) + max(skills[2:])
    if fair<=given:
        print("YES")
    else:
        print("NO")
level = int(input())
pass_levels = []
for x in range(2):
    passed = list(map(int,input().split()))
    pass_levels.extend(passed[1:])
pass_levels = set(pass_levels)
if len(pass_levels) == level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
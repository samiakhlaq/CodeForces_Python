point = int(input())
min_steps = 0
for x in range(5):
    min_steps = min_steps+ int(point/(5-x))
    point = point - (5-x)*int(point/(5-x))
print(min_steps)
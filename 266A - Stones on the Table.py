num_stones = int(input())
color = input()
min_stones = 0
for x in range (num_stones-1):
    if color[x] == color[x+1]:
        min_stones = min_stones+1
print(min_stones)
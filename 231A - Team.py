num_op = int(input())
input_set = list()
ability,solved = 0,0
for x in range(num_op):
    newlist = (list(map(int,input().split(" "))))
    input_set.extend([newlist])
for x in range (num_op):
    for y in range(3):
        if input_set[x][y] == 1:
            ability = ability+1
    if ability >=2:
        solved = solved +1 
    ability = 0
print(solved)

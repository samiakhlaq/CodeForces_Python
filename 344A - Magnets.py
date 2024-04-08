magnet = int(input())
c = 0
m = 0
for x in range(magnet):
    direction = int(input())
    if(m != direction):
        c+=1
    m = direction
print(c)

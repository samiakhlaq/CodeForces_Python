person,wall_height = map(int,input().split())
person_height = list(map(int,input().split()))
width = 0
for x in person_height:
    if x > wall_height:
        width+=2
    else:
        width+=1
print(width)
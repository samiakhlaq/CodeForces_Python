list_four = list(map(int,input().split()))
list_four[list_four.index(max(list_four))],list_four[0] = list_four[0],list_four[list_four.index(max(list_four))]
for x in range(1,4):
    print(list_four[0]-list_four[x],end=" ")

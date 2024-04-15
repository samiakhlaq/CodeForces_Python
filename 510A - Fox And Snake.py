row, column = map(int,input().split())
c = 0
for x in range (row):
    if x%2 == 0 :
        print("#"*column)
    else:
        if c%2 == 0:
            print("."*(column-1)+"#")
            c+=1
        else:
            print("#"+"."*(column-1))
            c= 0
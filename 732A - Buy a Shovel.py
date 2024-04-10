price,coin = map(int,input().split())
x=1
while 0!= ((price*x)%10)!= coin :
        x+=1
print(x)
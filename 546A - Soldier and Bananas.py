cost,num_dollars,num_bananas = map(int,input().split(" "))
needed_dollars = 0
for x in range(num_bananas):
    needed_dollars += (x+1)*cost
if needed_dollars < num_dollars:
    print(0)
else:
    print(needed_dollars-num_dollars)
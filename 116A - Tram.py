num_stops = int(input())
exist = 0
capacity = 0
for x in range(num_stops):
    exit,enter = map(int,input().split())
    exist = exist + enter - exit
    if exist>capacity:
        capacity = exist
print(capacity)
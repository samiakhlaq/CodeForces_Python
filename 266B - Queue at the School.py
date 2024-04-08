person,placement = map(int,input().split())
queue = input()
for x in range(placement):
    queue = queue.replace("BG","GB")
print(queue)
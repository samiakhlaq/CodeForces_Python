advanced = 0
perticipants, kth_place = map(int,input().split(" "))
scores = list(map(int, input().split(" ")))

for x in scores:
    if x >= scores[kth_place-1] and x!=0:
        advanced = advanced + 1
print(advanced)
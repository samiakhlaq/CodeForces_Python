given_num = input()
lucky_count = 0
for i in given_num:
    if i == '4'or i == '7':
        lucky_count+=1
if lucky_count == 4 or lucky_count == 7:
    print("YES")
else:
    print("NO")
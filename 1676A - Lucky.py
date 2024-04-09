num_test = int(input())
for x in range(num_test):
    ticket = list(map(int,input()))
    if sum(ticket[:3]) == sum(ticket[3:]):
        print("YES")
    else:
        print("NO")

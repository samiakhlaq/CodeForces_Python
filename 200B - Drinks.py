num_drinks = int(input())
percentage = list(map(int,input().split()))
total_percentage = 0
for x in percentage:
    total_percentage+=x
print(total_percentage/num_drinks)
def solve(num):
    digit = len(str(num))
    return 10**digit + 1
ntest = int(input())
for x in range(ntest):
    num = int(input())
    print(solve(num))
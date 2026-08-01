test_cases = int(input())

for _ in range(test_cases):
    a, b, c = map(int, input().split())

    if a + b == c or a + c == b or b + c == a:
        print("YES")
    else:
        print("NO")
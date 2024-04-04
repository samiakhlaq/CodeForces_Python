num_op = int(input())
x = 0
for _ in range(num_op):
    bit = input()
    if '+' in bit:
        x = x + 1
    else:
        x = x - 1
print(x)
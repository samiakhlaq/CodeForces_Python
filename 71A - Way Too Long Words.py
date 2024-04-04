def process(w):
    if len(w) <= 10:
        print(w)
    else:
        w = w[0] + str(len(w)-2) + w[-1]
        print(w)
num_op = int(input())
for x in range(num_op):
    word = input()
    process(word)
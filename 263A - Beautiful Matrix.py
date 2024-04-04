matrix = []
for i in range(5):
    matrix.extend([list(map(int, input().split()))])
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            index = i
            column = j
            break
print(abs(index-2)+ abs(column-2))
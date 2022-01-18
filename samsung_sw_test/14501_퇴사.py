N = int(input())

table = []

for _ in range(N):
    table.append(list(map(int, input().split())))

table.append([0,0])

for i in range(N-1, -1, -1):
    if N >= i + table[i][0]:
        table[i][1] = max(table[i+1][1], table[i][1] + table[i + table[i][0]][1])
    else:
        table[i][1] = table[i+1][1]

print(table[0][1])
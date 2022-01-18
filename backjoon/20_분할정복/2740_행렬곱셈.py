import sys

N, M = map(int, sys.stdin.readline().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

M, K = map(int, sys.stdin.readline().split())
B = []
for _ in range(M):
    B.append(list(map(int, sys.stdin.readline().split())))

result = []

for i in range(N):
    row = []
    for k in range(K):
        tmp = 0
        for j in range(M):
            # print(i, j, j, k)
            tmp += (A[i][j] * B[j][k])
        row.append(tmp)
    result.append(row)

for row in result:
    print(*row, sep=' ')
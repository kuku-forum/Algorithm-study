# import sys

# N = int(sys.stdin.readline())

# stairs = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# for i in range(1, N):
#     tmp = []
#     for j in range(10):
#         if j == 0:
#             tmp.append(stairs[i-1][1])
#         elif j == 9:
#             tmp.append(stairs[i-1][8])
#         else:
#             tmp.append(stairs[i-1][j-1] + stairs[i-1][j+1])
#     stairs.append(tmp)

# print(sum(stairs[-1])%1000000000)

import sys

N = int(sys.stdin.readline())

x = 9
answer = 9

if N > 1:
    x = 8
    answer = 8
    for i in range(1, N-1):
        x = 2*x - 1   
    answer = x*2 + (N-1)


print(answer%1000000000)
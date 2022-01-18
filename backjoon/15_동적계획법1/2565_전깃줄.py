import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
lines = []
lis = []

for _ in range(N):
    lines.append(list(map(int, sys.stdin.readline().split())))
lines.sort()

for line in lines:
    if not lis:
        lis.append(line[1])

    elif lis[-1] < line[1]:
        lis.append(line[1])
    else:
        idx = bisect_left(lis, line[1])
        lis[idx] = line[1]

print(N-len(lis))


# import sys

# N = int(sys.stdin.readline())
# lines = []
# dp = []

# for _ in range(N):
#     lines.append(list(map(int, sys.stdin.readline().split())))
#     dp.append(1)

# lines.sort()

# for i in range(1, N):
#     for j in range(i):
#         if lines[i][1] > lines[j][1]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(N - max(dp))
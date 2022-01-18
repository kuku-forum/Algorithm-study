import sys

N = int(sys.stdin.readline())
# liq = [0]
# dp = [0] + [0]*N

liq = []
dp = [0]*10000
# dp = {} # {0:1, 1: 3, }

for _ in range(N):
    liq.append(int(sys.stdin.readline()))


for i in range(0, N):
    if i == 1:
        dp[i] = liq[i]
    if i == 2:
        dp[i] = liq[i-1] + liq[i]
    # if i == 2:
    #     dp[2] = max(liq[0] + liq[2], liq[1] + liq[2])

    if i > 2:
        # dp[i] = max(liq[i]+liq[i-1]+dp[i-3], liq[i]+dp[i-2], dp[i-1])
        dp[i] = max(liq[i]+liq[i-1]+dp[i-3], liq[i]+dp[i-2])

print(dp)
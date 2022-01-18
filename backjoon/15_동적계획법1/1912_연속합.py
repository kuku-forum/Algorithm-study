import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp = [nums[0]]

for i in range(1, N):
    dp.append(max(nums[i], nums[i] + dp[i-1]))

# print(dp)
print(max(dp))
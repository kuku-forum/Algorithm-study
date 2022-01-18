import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [[1,1] for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        
        if nums[N-i-1] > nums[N-j-1]:
            dp[N-i-1][1] = max(dp[N-i-1][1], dp[N-j-1][1] + 1)

answer = [sum(num) for num in dp]
print(max(answer) - 1)
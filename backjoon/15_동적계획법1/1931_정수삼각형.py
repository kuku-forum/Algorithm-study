import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            nums[i][j] += nums[i-1][j]        
        elif j == i:
            nums[i][j] += nums[i-1][-1]
        else:
            nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])

print(max(nums[-1]))
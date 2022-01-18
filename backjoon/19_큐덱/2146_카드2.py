import sys
from collections import deque

nums = deque([i for i in range(1, int(sys.stdin.readline())+1)])

while True:
    if len(nums) == 1:
        print(nums[0])
        break

    nums.popleft()
    nums.rotate(-1)


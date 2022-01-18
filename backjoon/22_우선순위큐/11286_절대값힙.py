import sys
import heapq

N = int(sys.stdin.readline())
nums, heap = [], []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for num in nums:
    
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)
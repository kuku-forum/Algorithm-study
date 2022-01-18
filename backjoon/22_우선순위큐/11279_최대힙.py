import sys
import heapq

N = int(sys.stdin.readline())
nums, heap = [], []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for num in nums:
    if num > 0:
        heapq.heappush(heap, (-num, num))
    
    elif num == 0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
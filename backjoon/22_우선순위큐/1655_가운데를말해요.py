# import sys
# import heapq

# N = int(sys.stdin.readline())
# nums, min_heap, max_heap, result = [], [], [], []

# for _ in range(N):
#     nums.append(int(sys.stdin.readline()))

# for num in nums:
#     if len(min_heap) == len(max_heap):
#         heapq.heappush(min_heap, -num)
#     else:
#         heapq.heappush(max_heap, num)
        
#     if len(min_heap) > 0 and len(max_heap) > 0 and -min_heap[0] > max_heap[0]:
#         left = -heapq.heappop(min_heap)
#         right = heapq.heappop(max_heap)
        
#         heapq.heappush(min_heap, -right)
#         heapq.heappush(max_heap, left)
        
#     result.append(-min_heap[0])

# for i in result:
#     print(i)

import sys
import heapq

N = int(sys.stdin.readline())
nums, min_heap, max_heap, result = [], [], [], []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

heapq.heappush(min_heap, -nums[0])

for num in nums[1:]:
    if len(min_heap) ==1 and len(max_heap) == 0:
        result.append(-min_heap[0])
    
    if len(min_heap) > len(max_heap):    
        # print('#1')
        # print('min_heap', min_heap)
        # print('max_heap', max_heap)
        
        heapq.heappush(max_heap, num)
        left = -heapq.heappop(min_heap)
        result.append(left)
        heapq.heappush(min_heap, -left)
        # print('left: {}, num: {}'.format(left, num))
        
    elif len(min_heap) == len(max_heap):
        # print('#2')
        # print('min_heap', min_heap)
        # print('max_heap', max_heap)
        heapq.heappush(min_heap, -num)
        
        left = -heapq.heappop(min_heap)
        right = heapq.heappop(max_heap)
        
        # print('right: {}, left: {}'.format(right, left))
        
        if left <= right:
            heapq.heappush(min_heap, -left)
            heapq.heappush(max_heap, right)
            result.append(left)
        else:
            heapq.heappush(min_heap, -right)
            heapq.heappush(max_heap, left)
            result.append(right) 
        
for i in result:
    print(i)
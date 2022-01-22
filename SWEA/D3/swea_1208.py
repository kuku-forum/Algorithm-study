from my_package.hjtc import swea_tc
from heapq import heappush, heappop

for t in range(1, 11):
    
    answer = 0
    max_heap = []
    min_heap = []
    N = int(input())
    
    for num in map(int, input().split()):
        heappush(max_heap, (-num, num))
        heappush(min_heap, (num, num))
        
    for _ in range(N):
        max_val = heappop(max_heap)[1]
        max_val -=1
        heappush(max_heap, (-max_val, max_val))
        
        min_val = heappop(min_heap)[1]
        min_val += 1
        heappush(min_heap, (min_val, min_val))
    
    max_val = heappop(max_heap)[1]
    min_val = heappop(min_heap)[1]
    answer = max_val - min_val
    
    swea_tc(f'#{t} {answer}')   
    
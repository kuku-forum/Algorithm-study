'''
1 2 3 4 5 6 7 8 9 10
- 2 3 4 5 6 7 8 9 10 1 -> 1
- (2) 3 4 5 6 7 8 9 10 1 -> 3
- (9) 10 1 3 4 5 6 7 8  
'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
loc_list = list(map(int, sys.stdin.readline().split()))
deq = deque([i for i in range(1, N+1)])
answer = 0

for loc in loc_list:
    while True:
        if loc == deq[0]:
            deq.popleft()
            break
        else:
            loc_idx = deq.index(loc)
            if len(deq)-loc_idx >= loc_idx:
                deq.rotate(-loc_idx)
                answer += loc_idx
            else:
                deq.rotate(len(deq)-loc_idx)
                answer += (len(deq)-loc_idx)
print(answer)





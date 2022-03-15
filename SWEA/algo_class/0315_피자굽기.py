# from my_package.hjtc import swea_tc 
from collections import deque

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    que = deque()
    
    for idx, pizza in enumerate(map(int, input().split())):
        que.append([idx + 1, pizza])
        
    oven = deque()
    
    for _ in range(N):
        oven.append(que.popleft())
    
    while len(oven) > 1:
        
        while que and len(oven) != N:
            oven.append(que.popleft())
        
        idx, pizza = oven.popleft()
        pizza //= 2
        
        if pizza > 0:
            oven.append([idx, pizza])
                
    print(f'#{t} {oven[0][0]}')
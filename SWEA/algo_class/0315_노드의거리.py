from my_package.hjtc import swea_tc as print
from collections import deque

for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
        
    root, target = map(int, input().split())
    
    que = deque([])
    que.extend(graph[root])
    
    visited = [0 for _ in range(V + 1)]
    cnt = 0
    flag = False
    while que:
        
        if flag:
            break
        
        cnt += 1
        
        for _ in range(len(que)):
            node = que.popleft()
            
            if node == target:
                flag = True
                break
            
            for n in graph[node]:
                if visited[n] == 0:
                    que.append(n)
                    visited[n] = 1
    if not flag:
        cnt = 0
        
    print(f'#{t} {cnt}')
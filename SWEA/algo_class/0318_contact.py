from my_package.hjtc import swea_tc as print

from collections import deque

def bfs(graph, root):
    que = deque([root])
    visited = [0 for _ in range(101)]
    visited[root] = 1
    last_num = 0
    
    while que:
        last_num = max(que)
        for _ in range(len(que)):
            node = que.popleft()
            
            for new_node in graph[node]:
                if visited[new_node] == 0:
                    que.append(new_node)
                    visited[new_node] = 1
        
    return last_num


for t in range(1, 11):
    N, root = map(int, input().split())
    num_list = [[] for _ in range(101)]
    
    t_input = list(map(int, input().split()))
    
    for i in range(0, N-1, 2):
        num_list[t_input[i]].append(t_input[i+1])
    
    answer = bfs(num_list, root)
    print(f'#{t} {answer}')
    
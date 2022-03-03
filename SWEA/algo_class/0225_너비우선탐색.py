from collections import deque

def bfs(graph, root):
    visited = []
    que = deque([root])
    while que:    
        node = que.popleft()
        que_tmp = []
        
        if node not in visited:
            print(node)
            visited.append(node)
            
            for i in range(len(graph)):
                if node in graph[i]:
                    que_tmp.extend(graph[i])
            
            que_tmp.sort()
            que.extend(que_tmp)
            
    return visited

for t in range(1, int(input()) + 1):
    
    V, E = map(int, input().split())
    graph_list = []
    for _ in range(E):
        graph_list.append(list(map(int, input().split())))
    
    print(f'#{t}', *bfs(graph_list, 1), sep = ' ')
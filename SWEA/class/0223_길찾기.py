def dfs(graph, root):
    stack = [root]
    visited = [0 for _ in range(101)]
    
    while stack:
        node = stack.pop()
        
        if node == 99:
            return 1
        
        if visited[node] == 1:
            continue
        
        visited[node] = 1
        
        if graph[node]:
            stack.extend(graph[node])
        
    return 0


for _ in range(10):
    t, N = map(int, input().split())

    graph = [[] for _ in range(101)]
    node_list = list(map(int, input().split()))

    for i in range(0, len(node_list), 2):
        graph[node_list[i]].append(node_list[i + 1])

    print(f'#{t} {dfs(graph, 0)}')


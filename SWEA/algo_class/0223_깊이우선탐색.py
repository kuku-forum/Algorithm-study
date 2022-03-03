def dfs(graph, root):
    visited = []
    stack = [root]
    print(graph)
    while stack:
        print(stack)
        node = stack.pop()
        stack_tmp = []
        
        if node not in visited:
            print(node)
            visited.append(node)
            
            for i in range(len(graph)):
                if node in graph[i]:
                    stack_tmp.extend(graph[i])
            
            stack_tmp.sort(reverse=True)
            stack.extend(stack_tmp)
            
    return visited

for t in range(1, int(input()) + 1):
    
    V, E = map(int, input().split())
    node_list = [[] for _ in range(V + 1)]
    graph_list = []
    for _ in range(E):
        graph_list.append(list(map(int, input().split())))
    
    print(f'#{t}', *dfs(graph_list, 1), sep = ' ')
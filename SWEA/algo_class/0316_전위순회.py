def pre_order(node):
    if node == 0:
        return
    answer.append(node)
    
    pre_order(left[node])
    pre_order(right[node])
    
for t in range(1, int(input()) + 1):
    answer = []
    V = int(input())
    
    left = [0 for _ in range(V + 1)]
    right = [0 for _ in range(V + 1)]
    parent = [0 for _ in range(V + 1)]
    
    graph = list(map(int, input().split()))
    
    while graph:
        c = graph.pop()
        p = graph.pop()
        
        parent[c] = p
        
        if left[p] == 0:
            left[p] = c
        else:
            if left[p] > c:
                left[p], right[p] = c, left[p]
            else:
                right[p] = c
               
    pre_order(1)
    print(f'#{t}', *answer)
    
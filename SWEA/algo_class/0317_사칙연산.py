from my_package.hjtc import swea_tc as print



def search(n):
    if n:
        search(left[n])
        search(right[n])
            
        if node_list[n] == '*':
            node_list[n] = node_list[left[n]] * node_list[right[n]]
        elif node_list[n] == '+':
            node_list[n] = node_list[left[n]] + node_list[right[n]]
        elif node_list[n] == '-':
            node_list[n] = node_list[left[n]] - node_list[right[n]]
        elif node_list[n] == '/':
            node_list[n] = node_list[left[n]] / node_list[right[n]]


for t in range(1, 11):
    N = int(input())  
    
    left = [0 for _ in range(N + 1)]
    right = [0 for _ in range(N + 1)]
    node_list = [0 for _ in range(N + 1)]
    
    for _ in range(N):
        info = list(input().split())
        
        if len(info) == 4:
            node, op, L, R = int(info[0]), info[1], int(info[2]), int(info[3])
            left[node] = L
            right[node] = R
            
        elif len(info) == 3:
            node, op, L = int(info[0]), info[1], int(info[2])
            node_list[node] = op
            left[node] = L
            
        elif len(info) == 2:
            node, op = int(info[0]), info[1]
            node_list[node] = op
        
        if op.isdigit():
            node_list[node] = int(op)
        else:
            node_list[node] = op
    
    search(1)
    print(f'#{t} {int(node_list[1])}')
    
    
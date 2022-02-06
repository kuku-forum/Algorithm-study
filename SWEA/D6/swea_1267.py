from my_package.hjtc import swea_tc
from collections import deque

def bfs(root, board, re_board):
    que = deque(root)
    result = []
    visited = [False for _ in range(V + 1)]
    
    while que:
        node = que.popleft()
        result.append(node)
        visited[node] = True
        
        if board[node]:
            for new_node in board[node]:
                if visited[new_node] == False:
                    
                    for chk in re_board[new_node]:
                        
                        if not visited[chk]:
                            break
                    else:
                        que.append(new_node)
                        visited[new_node] = True

    return result


for t in range(1, 11):
    V, E = map(int, input().split())
    board = [[] for _ in range(V + 1)]
    re_board = [[] for _ in range(V + 1)]
    E_list = list(map(int, input().split()))
    
    for i in range(0, E*2, 2):
        board[E_list[i]].append(E_list[i+1])
        re_board[E_list[i+1]].append(E_list[i])
    
    root = []
    for idx, cell in enumerate(re_board[1:]):
        if not cell:
            root.append(idx+1)
            
    path = bfs(root, board, re_board)
    answer = ' '.join(map(str, path))
    swea_tc(f'#{t} {answer}')
    

        
    
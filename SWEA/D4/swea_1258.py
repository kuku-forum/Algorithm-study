from my_package.hjtc import swea_tc

def board_print(arr):
    for row in arr:
        print(row)
    print()
    
from collections import deque
T = int(input())

def bfs(board):
    result = []
    direct_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                que = deque([[i, j]])
                board[i][j] = 0
                width, height = 1, 1
                
                while que:
                    y, x = que.pop()
                    
                    for idx, direct in enumerate(direct_list):
                        dy, dx = direct[0], direct[1]
                        ny, nx = y + dy, x + dx
                        
                        if N > ny >= 0 and N > nx >= 0 and board[ny][nx] != 0:
                            board[ny][nx] = 0
                            que.append([ny, nx])
                            
                            if  i == ny:
                                width += 1
                            elif j == nx:
                                height += 1
                result.append([height, width])
    
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    return result


for t in range(1, T + 1):
    N = int(input())
    board = []
    
    for _ in range(N):
        board.append(list(map(int, input().split())))
        
    mat_list = bfs(board)
    num_mat = len(mat_list)
    answer = ' '.join(map(str, sum(mat_list, [])))
    
    swea_tc(f'#{t} {num_mat} {answer}')
'''
[[1, 2], [5, 1], [2, 6], [4, 6]]
4 1 2 5 1 2 6 4 6 -> X, answer: 
4 1 2 5 1 2 4 4 3

[1, 2, 3, 0, 0, 4, 5, 0]
[6, 7, 8, 0, 0, 0, 0, 0]
[9, 1, 2, 0, 0, 3, 0, 0]
[4, 5, 6, 0, 0, 7, 0, 0]
[0, 0, 0, 0, 0, 8, 0, 0]
[9, 1, 2, 3, 0, 4, 0, 0]
[5, 6, 7, 8, 0, 9, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0]
    '''
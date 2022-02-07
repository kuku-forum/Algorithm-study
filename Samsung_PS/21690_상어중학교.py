'''
검은색 블록: -1
무지개 블록: 0
일반 블록: M

인접: |r1 - r2| + |c1 - c2| = 1
> 동서남북

그룹: 
> 일반 블록 하나가 무조건 필요
> 일반 블록 모두 같음, 검은색 블록X, 무지개 블록O, 
> 블록의 개수는 2보다 크거나 같아야
> 블록 그룹의 기준: 일반블록 최소 행 -> 최소 열

게임:
> 그룹찾기: 최대 그룹 -> 최다 무지개 -> 최대 행 -> 최대 열
> 제거 및 제곱 획득
> 중력(검은색 제외)
> 90도 반시계 회전
> 중력
'''

from collections import deque


def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]


def gravity(board):
    N = len(board)
    
    for x in range(N):
        y = N - 1
        
        while y >= 1:
            if board[y][x] == -2:
                dy = y - 1
                
                while dy >= 0:
                    
                    if board[y][x] != -2:
                        break
                    
                    if board[dy][x] == -1:
                        if dy - 1 >= 0:
                            y = dy - 1
                            dy = y - 1
                        else:
                            break
                    
                    elif board[dy][x] != -2:
                        board[y][x], board[dy][x] = board[dy][x], -2
                        break
                        
                    else:
                        dy -= 1
            y -= 1
    return board


def bfs(board):
    global answer
    final_group = []
    pre_rainbow, pre_block_cnt, fin_y, fin_x = -1, -1, -1, -1
    
    for i in range(N):
        for j in range(N):
            change = False
            
            if board[i][j] > 0:
                
                color = board[i][j]
                que = deque([(i, j)])
                visited[i][j] = 1
                
                std_y, std_x = 0xffff, 0xffff
                rainbow, block_cnt = 0, 1
                
                tmp_group = [(i, j)]
                
                while que:
                    y, x = que.popleft()
                
                    if board[y][x] > 0 and (std_y, std_x) > (y, x):
                        std_y, std_x = y, x
                            
                    for dy, dx in direct_list:
                        ny = y + dy
                        nx = x + dx
                        
                        if N > ny >= 0 and N > nx >= 0 and board[ny][nx]  >= 0 and visited[ny][nx] == 0:
                            if board[ny][nx] == 0 or board[ny][nx] == color:
                                que.append((ny, nx))
                                visited[ny][nx] = 1
                                tmp_group.append((ny, nx))
                                block_cnt += 1
                                
                                if board[ny][nx] == 0:
                                    rainbow += 1
                  
                for ry, rx in tmp_group:
                    visited[ry][rx] = 0
                
                if block_cnt > 1:
                    
                    if not final_group:
                        change = True
                    
                    elif block_cnt > pre_block_cnt:
                        change = True
                        
                    elif block_cnt == pre_block_cnt:
                        if rainbow > pre_rainbow:
                            change = True
                            
                        elif rainbow == pre_rainbow:
                            if (std_y, std_x) > (fin_y, fin_x):
                                change = True
                                
                if change:
                    final_group = tmp_group
                    pre_block_cnt = block_cnt
                    pre_rainbow = rainbow
                    fin_y = std_y
                    fin_x = std_x    
                    
    if not final_group:
        return True
    else:
        for ry, rx in final_group:
            board[ry][rx] = -2
            
        answer += len(final_group)**2
        return False

    
answer = 0
direct_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]

N, M = map(int, input().split())
board = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    board.append(list(map(int, input().split())))

while True:
    if bfs(board):        
        break
    board = gravity(board)
    board = rot270(board)
    board = gravity(board)

print(answer)
# 되는 조건
# i == i-1 == i-2 == i-L
# i == (i-1 == i-2 == i-L) + 1
# i == (i-1 == i-2 == i-L) + 1 -> unique
from pprint import pprint
N, L = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    

visited = [[0 for _ in range(N)] for _ in range(N)]
stair_list = []

def runway_row(root, board):
    y, x = root[0], root[1]
    # 초기값 선정
    init_val = board[y][x]
    
    # x를 하나씩 증가시키며 검사
    while N > x:
        # 초기값보다 값이 커질 경우
        if board[y][x] > init_val:
            # 2 차이 이상 나면 False 
            if abs(board[y][x] - init_val) >= 2:
                return False
            
            # L의 범위만큼 뒤로 가서 경사로를 놓을 수 있는지 확인
            for nx in range(x - 1, x - L - 1, -1):
                # 뒤로 가다가 board 범위를 벗어나면 False
                if 0 > nx:
                    return False
                
                # 뒤로가다 초기값이랑 다를경우 False 혹은 이미 방문했던 경사로일경우 False
                if board[y][nx] != init_val or visited[y][nx] == 1:
                    return False
                # 뒤로 잘 가진다면 stair_list에 경사로를 놓을 위치를 append
                else:
                    stair_list.append([y, nx])
            
            # 경사로 설치가 끝났으니, visied에 방문했다고 표시
            for uy, ux in stair_list:
                visited[uy][ux] = 1
            
            # 새로운 초기값 설정
            init_val = board[y][x]
            
        
        # 초기값보다 값이 작아질 경우
        elif board[y][x] < init_val:
            # 2 차이 이상 나면 False 
            if abs(board[y][x] - init_val) >= 2:
                return False
            
            # 앞으로가는 경우는 고려할게 더 있어서 fx를 따로 할당
            fx = x
            # 현재 위치를 초기값으로 선정 및 경사로가 놓일위치이므로 stair_list에 append
            init_val = board[y][fx]
            stair_list.append([y, fx])
            
            # 현재위치를 제외하고 경사로 길이만큼 앞으로 전진(L - 1 만큼)
            for nx in range(fx + 1, fx + L, 1):
                # board를 넘어가면 False
                if nx >= N:
                    return False
                
                # 초기값이랑 값이 달라지거나 방문했다면 False
                if board[y][nx] != init_val or visited[y][nx] == 1:
                    return False
                # 경사로를 넣을 위치를 append
                else:
                    stair_list.append([y, nx])
                    
                # 앞으로 가는 x인 fx를 더해줌
                fx += 1
            
            # 경사로 놓아진 위치에 방문 표시
            for uy, ux in stair_list:
                visited[uy][ux] = 1
            
            # 초기값 다시 선정
            init_val = board[y][x]
        
        # 앞으로 전진
        x += 1
    return True


def runway_col(root, board):
    y, x = root[0], root[1]
    init_val = board[y][x]
    
    while N > y:
        if board[y][x] > init_val:
            if abs(board[y][x] - init_val) >= 2:
                return False
            
            for ny in range(y - 1, y - L - 1, -1):
                if 0 > ny:
                    return False
                if board[ny][x] != init_val or visited[ny][x] == 1:
                    return False
                else:
                    stair_list.append([ny, x])
                    
            for uy, ux in stair_list:
                visited[uy][ux] = 1
                
            init_val = board[y][x]
            
        elif board[y][x] < init_val:
            if abs(board[y][x] - init_val) >= 2:
                return False
            
            fy = y
            init_val = board[fy][x]
            stair_list.append([fy, x])
            for ny in range(fy + 1, fy + L, 1):
                if ny >= N:
                    return False
                if board[ny][x] != init_val or visited[ny][x] == 1:
                    return False
                else:
                    stair_list.append([ny, x])
                fy += 1
            
            for uy, ux in stair_list:
                visited[uy][ux] = 1
                
            init_val = board[y][x]
            
        y += 1
    
    return True

answer = 0

# row 탐색
for i in range(N):
    if runway_row([i, 0], board):
        answer += 1

# visited 초기화
for y, x in stair_list:
    visited[y][x] = 0
stair_list = []

# col 탐색
for j in range(N):
    if runway_col([0, j], board):
        answer += 1

# visited 초기화
for y, x in stair_list:
    visited[y][x] = 0
stair_list = []

print(answer)
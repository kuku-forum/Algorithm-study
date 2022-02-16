'''

! 주의 !
> 배수를 할때 마지막 부분도 배수가 잘 되었는지 확인
> 원판에 수가 남았있는지를 체크하고 처리를 해야함 -> 원판이 없는데 평균처리를 하다 zero division error 발생
> 인접함을 진행할떄, 범위를 그대로 M > j >= 0 으로 해야함, 만약 -1까지 가능하다고 적는다면, 수가 계속 작아지니 인접함을 찾지 못함

ex) 아래 예
> 1 0 1 1
> 0 0 0 1
> 0 0 0 0 

1. x의 배수인 원판을 d방향(0 시계, 1 반시계)으로 k칸 회전
2. 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
3_1. 있는 경우, 원판에서 인접하면서 같은 수를 모두 지운다.
3_2. 없는 경우, 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
4. 원판을 T번 회전시킨 후 원판에 적힌 수의 합 반환
'''
    
from collections import deque

N, M, T = map(int, input().split())

board = [deque(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(T)]
direction_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs():
    flag = True
    
    for i in range(N):
        for j in range(M):
            
            if board[i][j] == 0:
                continue
            
            num_init = board[i][j]
            que = deque([[i, j]])
            
            while que:
                r, c = que.popleft()    
                for dr, dc in direction_list:
                    nr = r + dr
                    nc = c + dc
                    
                    if nc == M:
                        nc = 0
                    elif nc == -1:
                        nc = M - 1
                    
                    
                    if N > nr >= 0 and M > nc >= 0:
                        if num_init == board[nr][nc]:
                            que.append([nr, nc])
                            board[nr][nc] = 0
                            board[r][c] = 0
                            flag = False
                            
                    # if nc >= 0:
                    #     nc %= M
                        
                    # if N > nr >= 0 and M > nc >= -1:
                    #     if num_init == board[nr][nc]:
                    #         que.append([nr, nc])
                    #         board[nr][nc] = 0
                    #         board[r][c] = 0
                    #         flag = False
                   
    return flag


def div_board():
    cnt = 0
    total_val = 0
    pos_list = []
    
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt += 1
                total_val += board[i][j]
                pos_list.append([i, j])
    
    if cnt == 0:
        return True
    
    mean_val = total_val/cnt
    
    for i, j in pos_list:
        if board[i][j] > mean_val:
            board[i][j] -= 1
        
        elif mean_val > board[i][j]:
            board[i][j] += 1
    
    return False


for x, d, k in command:
    k %= M
    d = -1 if d == 1 else 1
    d *= k
    cnt = 1
    
    while N >= x*cnt:
        x_idx = x*cnt - 1
        board[x_idx].rotate(d)
        cnt += 1
    
    if bfs():
        if div_board():
            break
    
print(sum(map(sum, board)))
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

# 270도 함수
def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

# 중력 작용: 두 포인터를 통해 진행
# y가 빈공간을 만나면 dy가 움직임 -> dy가 블록을 만나면 y랑 교체해주면서 계속 탐색
def gravity(board):
    N = len(board)
    
    # (N-1, [0 ~ N-1]) 열을 하나씩 증가하여 가장 아래 행부터 모든 영역 탐색
    for x in range(N):
        y = N - 1
        
        # y가 두번째 행 까지 올라오도록 함
        while y >= 1:
            
            # -2(빈공간)을 만날경우 dy(두번째 포인터) 생성 
            if board[y][x] == -2:
                dy = y - 1
                
                # dy가 첫번째 행 끝까지 올라가도록 작동
                while dy >= 0:
                    
                    # y가 빈공간을 만나면 break
                    if board[y][x] != -2:
                        break
                    
                    # -1(고정)을 만날경우 y를 dy의 위로 올려주고 dy는 y보다 한칸 더 올려줌
                    if board[dy][x] == -1:
                        if dy - 1 >= 0:
                            y = dy - 1
                            dy = y - 1
                        else:
                            break
                    
                    # dy가 블록을 만나면 dy블록엔 -2(빈공간) 설치 하고 y엔 dy블록 가져옴 그리고 break
                    elif board[dy][x] != -2:
                        board[y][x], board[dy][x] = board[dy][x], -2
                        break
                    
                    # 위에 사항이 없을경우 빈공간을 만난거라 볼 수 있으므로 dy를 계속 위로 올려줌
                    else:
                        dy -= 1

            # 다 끝났으면 y를 한칸 올려준 후 다시 진행
            y -= 1
    return board


# bfs를 통해 블록그룹을 찾음
def bfs(board):
    global answer
    # 이전에 찾은 블록그룹(선정된 그룹)과 현재 찾은 블록 그룹 비교를 위해 아래 변수 선언
    final_group = []
    pre_rainbow, pre_block_cnt, fin_y, fin_x = -1, -1, -1, -1
    
    # 모든 지역 탐색
    for i in range(N):
        for j in range(N):
            change = False
            
            # 컬러 블록을 만났을 경우 bfs 탐색
            if board[i][j] > 0:
                
                # 초기 컬러 설정 및 방문, que 설정
                color = board[i][j]
                que = deque([(i, j)])
                visited[i][j] = 1
                
                # 가장 작은 기준블록을 찾기위해 설정
                std_y, std_x = 0xffff, 0xffff
                
                # 무지개블록과, 찾은 전체 블록수를 찾기위한 변수 선언
                rainbow, block_cnt = 0, 1
                
                # 현재 찾은 블록그룹
                tmp_group = [(i, j)]
                
                while que:
                    y, x = que.popleft()

                    # bfs을 통해 찾은 블록이 컬러블록이고, 행렬 조건에 부합하면 기준 블록 교체
                    if board[y][x] > 0 and (std_y, std_x) > (y, x):
                        std_y, std_x = y, x
                    fdfd
                    # 전방 탐색
                    for dy, dx in direct_list:
                        ny = y + dy
                        nx = x + dx
                        
                        # 탐색한 블록이 무지개 혹은 컬러 블록이고 방문하지 않았다면 방문
                        # 무지개 거나, 컬러가 같은경우 방문
                        if N > ny >= 0 and N > nx >= 0 and board[ny][nx]  >= 0 and visited[ny][nx] == 0:
                            if board[ny][nx] == 0 or board[ny][nx] == color:
                                que.append((ny, nx))
                                visited[ny][nx] = 1
                                
                                # 현재 그룹에 추가하고, 블록 갯수 증가
                                tmp_group.append((ny, nx))
                                block_cnt += 1
                                
                                # 무지개 블록일 경우 무지개 카운트 증가
                                if board[ny][nx] == 0:
                                    rainbow += 1
                
                # 탐색이 다 끝나면, 방문했던것들 초기화 진행  
                for ry, rx in tmp_group:
                    visited[ry][rx] = 0
                
                # 블록그룹이 2 이상일 경우 아래 진행
                if block_cnt > 1:
                    
                    # 만약 첫음 찾은 블록그룹이라면 현재 블록그룹을 final_group 으로 설정
                    if not final_group:
                        change = True
                    
                    # 블록 개수 비교
                    elif block_cnt > pre_block_cnt:
                        change = True
                    
                    # 무지개 블록 비교
                    elif block_cnt == pre_block_cnt:
                        if rainbow > pre_rainbow:
                            change = True
                            
                        # 기준 블록 행렬 비교
                        elif rainbow == pre_rainbow:
                            if (std_y, std_x) > (fin_y, fin_x):
                                change = True
                
                # 비교 결과 변경해야한다면
                # 현재 그룹이 최종 그룹 등등 전부 교체                
                if change:
                    final_group = tmp_group
                    pre_block_cnt = block_cnt
                    pre_rainbow = rainbow
                    fin_y = std_y
                    fin_x = std_x    
    
    # 모든 탐색을 끝냈는데 찾은 그룹이 없으면 종료를 위한 True 반환
    if not final_group:
        return True
    else:
        # 최종 그룹에서 board 제거
        for ry, rx in final_group:
            board[ry][rx] = -2
        
        # answer 값 추가
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
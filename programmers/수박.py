from collections import deque

# 보통 너비, 높이 정해줌, 해당 값 설정
W, H = map(int, input().split())

# board에 전체 값을 받아옴
board = [list(map(int, input().split())) for _ in range(H)]

# 처음 수박이 있는 경우를 다 찾음
start_lst = deque([])
for i in range(H):
    for j in range(W):
        if board[i][j] == 1:
            start_lst.append([i, j])

# 상화좌우 내 방향
directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def solution():
    # deque인 que로 지정, day를 0으로 설정
    que = start_lst
    day = 0
    
    # que가 없을때 까지 반복
    while que:
        # que에 담아있는 수박 수만큼 진행, 처음엔 초기 수박 수만큼만 loop가 돎
        for _ in range(len(que)):
            
            # que에 맨 앞부분 좌표를 추출(FIFO)
            r, c = que.popleft()
            
            # 상하좌우 탐색
            for dr, dc in directions:
                # 새로운(인접한) r, c 좌표 생성
                nr = r + dr
                nc = c + dc
                
                # board의 범위를 넘지 않고 수박이 안익었을 경우
                # 해당 영역을 1값으로 바꿔준 후
                # que의 뒤에 좌표 넣음
                if H > nr >= 0 and W > nc >= 0 and board[nr][nc] == 0:
                    board[nr][nc] = 1
                    que.append([nr, nc])
        
        # que에 담긴 수만큼 다 돌았으니 day가 +1 증가
        day += 1
        
    return day

# 다 익어 있을 경우
if len(start_lst) == W*H:
    print(0)

# 수박이 없을 경우
elif len(start_lst) == 0:
    print(-1)
# 하나라도 수박이 있을 경우
else:
    print(solution())
    
    
'''
#0
000000
000000
000000
000001

#1
000000
000000
000002
000021

#2
000000
000003
000032
000321

#3
000004
000043
000432
004321

#4
000011
000111
001111
011111

#5
000111
001111
011111
111111

#6
001111
011111
111111
111111

#7
011111
111111
111111
111111

#8
987654
876543
765432
654321
'''
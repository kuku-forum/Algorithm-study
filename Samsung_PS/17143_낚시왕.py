'''
낚시왕 루틴
> 낚시왕이 오른쪽으로 한 칸 이동한다.
> 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 
    상어를 잡으면 격자판에서 잡은 상어가 사라진다.
> 상어가 이동한다.

상어 루틴
> 주어진 속도 이동
> 벽 만나면 반대 방향으로 이동
> 상어 '이동 후' 같은칸의 상어는 큰 상어에게 잡아먹힘
> 1:위, 2: 아래, 3: 오른, 4: 왼쪽 
    -> 변경: 0:위, 1: 아래, 2: 오른, 3: 왼쪽 
    -> 변경: 0:위, 1: 오른, 2: 아래, 3: 왼쪽

R, C, M(상어 수)
(r, c), s, d, z 
위치, 속력, 방향, 크기

방향 
'''
# from collections import defaultdict
# from pprint import pprint

# def print_board(arr):
#     for row in arr:
#         print(row)
#     print()

# 값들을 받는다
R, C, M = map(int, input().split())

board = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
shark_list = [[] for _ in range(M)]

for m in range(M):
    r, c, s, d, z = map(int, input().split())
    d -= 1
    
    # 방향 전환이 유용하도록 d의 위치를 변경
    if d == 1: d = 2
    elif d == 2: d = 1
    
    # board의 값을 받는다
    board[r][c].append(m)
    # shark의 메타 데이터를 리스트를 통해 받는다.
    # 0번 상어, 1번 상어...
    shark_list[m] = (r, c, s, d, z)

# 방향을 남 동 북 서 로 설정
direct_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 낚시
def fisherman(pos):
    score = 0
    catch = []
    # 맨 윗줄 부터 board를 통해 상어를 찾는다.
    for i in range(R + 1):
        if board[i][pos]:
            catch, board[i][pos] = board[i][pos], []
            break
    # 상어를 찾으면, 해당 성어의 무게마큼 score 획득
    if catch:
        score += shark_list[catch[0]][-1]
        shark_list[catch[0]] = []
    
    # score 반환
    return score


# 상어 이동
def wave():
    # 상어 idx(0 ~ M-1)를 통해 하나씩 이동시킨다.
    for shark in range(M):
        # 상어 리스트에서 상어가 있을경우 메타 데이터 수집
        if shark_list[shark]:
            i, j, s, d, z = shark_list[shark]
            # 선택된 상어의 리스트 초기화
            shark_list[shark] = []
            # board에서 선택된 상어 제거

            del board[i][j][board[i][j].index(shark)]
            di, dj = direct_list[d]
            
            # s만큼 상어 이동 및 범위를 벗어날 경우 방향 전환
            for _ in range(s):
                if R + 1 > i + di >= 1 and C + 1 > j + dj >= 1:
                    i += di
                    j += dj        
                else:
                    d = (d + 2)%4
                    di, dj = direct_list[d]
                    i += di
                    j += dj
            
            # 초기화한 상어 리스트에 변경된 상어 메타 데이터 설정
            shark_list[shark] = (i, j, s, d, z)
            # board에 상어 위치
            board[i][j].append(shark)
    
    # board를 전체 다 돌면서 상어가 2개 이상인 것을 찾음
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if len(board[i][j]) >= 2:
                # weight 리스트를 제작하여 해당 상어의 idx와 무게 정보 반환
                wieght_list = []
                for shark in board[i][j]:
                    wieght_list.append((shark, shark_list[shark][-1]))
                
                # 상어 무게를 중심으로 sort
                wieght_list.sort(key=lambda x: x[1])
                # 가장 강한 상어는 무게가 제일 큰 상어
                strong_shark, _ = wieght_list[-1]
                
                # 무게가 제일 큰 상어를 제외한 나머지 상어들은 상어리스트에서 제거
                for shark, _ in wieght_list[:-1]:
                    shark_list[shark] = []
                
                # board에는 가장 강한 상어만 삽입
                board[i][j] =[strong_shark]


# C(가로)만큼 반복   
answer = 0
for move in range(1, C + 1):
    answer += fisherman(move)
    wave()
    
print(answer)
    
            
    
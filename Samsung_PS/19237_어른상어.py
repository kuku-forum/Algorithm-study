'''
1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다
맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다
1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고
자신의 냄새를 그 칸에 뿌린다
냄새는 상어가 k번 이동하고 나면 사라진다

이동 방향을 결정할 때는
인접한 칸 중 아무 냄새가 없는 칸의 방향
그런 칸이 없으면 자신의 냄새가 있는 칸의 방향
특정한 우선순위에 따라 자신의 냄새가 있는 칸의 방향
가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.

1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지

1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽

> 상어 위치 dict
> board를 통한 중복 체크 
> 우선순위 dict

1. 본인자리 냄새 뿌림
2. 상하좌우 확인 -> 빈자리 있을경우 이동 -> 많으면 우선순위 체크
2_2. 빈자리 없을 경우 -> 자기 위치 확인
2_3. 자기 위치가 많으면 -> 우선순위 체크
2-4. 방향 전환 및 이동
3. 이동후 중복이면 제거
4. 순회하면 count 제거
'''

from collections import defaultdict

meta_info = {}
board_scent =[]
board_shark = []
direction_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
priority_dic = defaultdict(list)

N, M, K = map(int, input().split())

for i in range(N):
    row_scent = []
    row_shark = []
    for j, shark in enumerate(map(int, input().split())):
        if shark > 0:
            meta_info[shark] = [i, j]
            row_scent.append([shark, K])
            row_shark.append([shark])
        else:
            row_scent.append([0, 0])
            row_shark.append([])
            
    board_scent.append(row_scent)
    board_shark.append(row_shark)


for i, tmp in enumerate(map(int, input().split())):
    meta_info[i + 1].append(tmp - 1)

    
for i in range(1, M + 1):
    for j in range(4):
        row = []
        for d in map(int, input().split()):
            row.append(d - 1)
        priority_dic[i].append(row)


def wave():
    for shark in range(1, M + 1):
        if shark not in meta_info:
            continue
        
        r, c, d = meta_info[shark]
        board_shark[r][c] = []
        empty_list = []
        my_list = []
        priority_list = priority_dic[shark][d]
        priority = None
        
        for idx_d in range(4):
            dr, dc = direction_list[idx_d]
            nr = r + dr
            nc = c + dc
            
            if N > nr >= 0 and N > nc >= 0:
                if board_scent[nr][nc][0] == shark:
                    my_list.append(idx_d)
                
                elif board_scent[nr][nc][0] == 0:
                    empty_list.append(idx_d)
                    
        if empty_list:
            for pri_idx in priority_list:
                if pri_idx in empty_list:
                    dr, dc = direction_list[pri_idx]
                    nr = r + dr
                    nc = c + dc
                    priority = pri_idx
                    break
                    
                    
        elif my_list:
            for pri_idx in priority_list:
                if pri_idx in my_list:
                    dr, dc = direction_list[pri_idx]
                    nr = r + dr
                    nc = c + dc
                    priority = pri_idx
                    break
        
        meta_info[shark] = [nr, nc, priority]
        board_shark[nr][nc].append(shark)            
                    
            
def double_decent():
    for i in range(N):
        for j in range(N):
            
            if board_shark[i][j]:
                
                if len(board_shark[i][j]) >= 2:
                    board_shark[i][j].sort()
                    
                    for _ in range(len(board_shark[i][j]) - 1):
                        rm_shark = board_shark[i][j].pop()
                        del meta_info[rm_shark]
                        
            if board_scent[i][j][1] > 0:
                board_scent[i][j][1] -= 1
                
                if board_scent[i][j][1] == 0:
                    board_scent[i][j][0] = 0

            
def set_pos():
    for shark in range(1, M + 1):
        if shark not in meta_info:
            continue
        
        r, c, _ = meta_info[shark]
        board_scent[r][c] = [shark, K]


flag = 0
while 1000 > flag:
    wave()
    double_decent()
    set_pos()
    
    flag += 1
    
    if len(meta_info) == 1:
        break    
else:
    flag = -1
    
print(flag)

'''
1. 활성화 시킬 위치 선정 (combinantions)
2. BFS 진행
3. 모두 다 퍼졌는지 확인

주의:
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다
모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간(비활성이 활성 될 필욘 없음)
'''

from collections import deque


# combination 생성기
def gen_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i + 1:], n - 1):
            result.append([elem] + C)
    return result


# 0은 빈 칸, 1은 벽, 2는 바이러스
def bfs(board, act_virus, rm_room):
    
    # 방문 확인용 visited 생성: 전부 -1 선언
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    
    # 선택된 바이러스는 0으로 선언
    # 선택되지 않은 바이러스(비활성화)는 -2로 선언
    for dis_virus in virus_pos:
        if dis_virus not in act_virus:
            visited[dis_virus[0]][dis_virus[1]] = -2
        else:
            visited[dis_virus[0]][dis_virus[1]] = 0
    
    
    # (1, 2, 3, 4, 5)
    # (1, 2, 3), (1, 2, 4)
    # deque([1,2,3])
    que = deque(act_virus)
    # 총 걸린 시간
    total_time = 0
    
    while que:
        # cnt += 1
        # for _ in range(len(que)):
            
        y, x = que.popleft()

        # 제거할 방이 0이 되었을 경우 반환
        if rm_room == 0:
            return total_time
        
        for dy, dx in direct_list:
            ny = y + dy
            nx = x + dx
            
            # (ny, nx)가 board의 범위를 넘지않고, 
            # 빈공간 혹은 비활성 바이러스일 경우 탐색 진행
            if N > ny >= 0 and N > nx >= 0 and board[ny][nx] != 1:
                
                # 빈공간일 경우
                # que에 집어넣고 total_time의 값 선정
                # 제거해야할 방 갯수 줄임
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append([ny, nx])
                    total_time = visited[ny][nx]
                    rm_room -= 1
                
                # 비활성 바이러스일 경우
                # 활성 바이러스로 변경
                # rm_room은 줄이지 않고 que에만 넣음
                elif visited[ny][nx] == -2:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append([ny, nx])
    
    # 제거할 rm이 남아있지만 더이상 제거 불가
    # 답이 없다는 의미로 초기값(가장큰값) 반환
    return 0xffff


N, M = map(int, input().split())
board_list = []
# 바이러스 위치 찾기
virus_pos = []
# 빈방의 수(제거할 대상) 찾기
rm_cnt = 0
# 방향
direct_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# 가장 큰 값 세팅
answer = 0xffff 

for i in range(N):
    row = []
    for j, val in enumerate(map(int, input().split())):
        row.append(val)
        
        if val == 2:
            virus_pos.append([i, j])
        elif val == 0:
            rm_cnt += 1
            
    board_list.append(row)
    

# 처음에 제거할 대상이 없다면 0 출력
if rm_cnt == 0:
    print(0)
else:        
    # combination을 통해 선정된 바이러스를 bfs로 전환
    # min을 통해 가장 작은 값을 찾음
    for virus_combi in gen_combi(virus_pos, M):
        act_time = bfs(board_list, virus_combi, rm_cnt)
        answer = min(answer, act_time)

    # 답이 초기 값을 경우 -1 출력
    print(answer if 0xffff > answer else -1)
'''
1. 빈공간(0) 부분을 zero list에 담는다.
2. zero로 만들 수 있는 경우의 수를 출력한다.
3. 해당 경우의 수로 벽을 세운다.
4. 벽을 세운 보드에서 bfs를 진행하여 바이러스를 퍼트린다.
5. 모든 바이러스가 퍼진 후 빈 공간을 카운트한다.
'''

from collections import deque

N, M = map(int, input().split())

board_lst = [[0 for _ in range(M)] for _ in range(N)]
zero_lst = []
one_lst = []
root = []
direct_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 0의 좌표 추출하여 zero list 제작 (빈 공간)
# 1의 좌표 추출하여 1 리스트 제작
# 2의 좌표는 바이러스 이므로 초기 바이라서 제작
for i in range(N):
    for j, factor in enumerate(map(int, input().split())):
        if factor == 0:
            zero_lst.append([i, j])
            continue
        if factor == 1:
            one_lst.append([i, j])
        if factor == 2:
            root.append([i, j])
        board_lst[i][j] = factor


# combination 함수
# combi(arr[1, 2, 3, 4, 5], 3)
def combi(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(): # 5: 0~5
        elem = arr[i] # arr[0] -> 1
        
        # combi(arr[2, 3, 4, 5], 2)
        # combi(arr[3, 4, 5], 1) 
        # combi(arr[4, 5], 0) [[]]
        for C in combi(arr[i+1:], n-1):
            result += [[elem] + C]
            
    return result


for i in range(N):
    for j in range(1 + 1, N):
        for k in range(j +1, N):
            'do'

# zero를 combination하여 empty-lst를 제작한다.
empty_lst = combi(zero_lst, 3)
answer = 0

def bfs(board, root, empty_lst):
    global answer
    
    # 방문여부를 확인하기위해 visited 제작
    visited = [[0 for _ in range(M)] for _ in range(N)]
    
    # 바이러스가 시작할 위치
    # 기존 벽이 있던 위치
    for y, x in root:
        visited[y][x] = 1
    for y, x in one_lst:
        visited[y][x] = 1
        
    # empty lst만큼 진행
    for i in range(len(empty_lst)):
        
        # empty list의 값들을 토해 board에 벽을 설치
        for empty in empty_lst[i]:
            board[empty[0]][empty[1]] = 1
        
        rm_visited = []
        # 내가 만든 벽이 있던 위치를 초기에 방문했다고 설정 
        for empty in empty_lst[i]:
            visited[empty[0]][empty[1]] = 1
            
        que = deque(root)
        while que:
            y, x = que.popleft()

            # 4방향 탐색
            for direct in direct_lst:
                ny = y + direct[0]
                nx = x + direct[1]

                # 범위가 벗어나지 않고, 방문하지 않았다면 접근
                if N > ny >= 0 and M > nx >= 0 and visited[ny][nx] == 0:
                    # 빈공간일 경우 방문처리 및 que에 추가
                    if board[ny][nx] == 0:
                        visited[ny][nx] = 1
                        que.append([ny, nx])
                        rm_visited.append([ny, nx])
        
        # 확산이 끝난 후 모든 칸을 순회하며 빈공간 갯수 카운트
        cnt = 0
        for row in visited:
            for elem in row:
                if elem == 0:
                    cnt += 1

        # 최댓값 설정
        answer = max(answer, cnt)

        # 내가 설치했던 벽을 치워줌(리셋 작업)
        for empty in empty_lst[i]:
            board[empty[0]][empty[1]] = 0
            visited[empty[0]][empty[1]] = 0
            
        for vy, vx in rm_visited:
            visited[vy][vx] = 0


bfs(board_lst, root, empty_lst)
print(answer)




# 메모리: 136468kb
# 시간: 940ms

# from collections import deque
# from copy import deepcopy


# # combination 함수
# def combi(arr, n):
#     result = []
#     if n == 0:
#         return [[]]

#     for i in range(len(arr)):
#         elem = arr[i]
#         for C in combi(arr[i+1:], n-1):
#             result += [[elem] + C]

#     return result


# N, M = map(int, input().split())
# arr = []
# vir_queue = deque()
# wall_tmp = []
# d=[(0, 1), (0,-1), (1, 0), (-1, 0)]
# for n in range(N):
#     arr.append(list(map(int, input().split())))
#     for m in range(M):
#         if arr[n][m]==2:
#             vir_queue.append((n, m))
#         elif arr[n][m]==0:
#             wall_tmp.append((n, m))
# vir_queue1 = deepcopy(vir_queue)

# def bfs():
#     while vir_queue:
#         x,y = vir_queue.popleft()
#         for k in range(4):
#             nx = x+d[k][0]
#             ny = y+d[k][1]
#             if nx in range(N) and ny in range(M) and arr1[nx][ny] == 0:
#                 arr1[nx][ny] = 2
#                 vir_queue.append((nx, ny))

# wall_combi = combi(wall_tmp,3)
# max_safe = 0
# for tmp in wall_combi:
#     arr1 = deepcopy(arr)
#     for point in tmp:
#         x, y = point
#         arr1[x][y] = 1
#     vir_queue = deepcopy(vir_queue1)
#     bfs()
#     ans = 0
#     for row in arr1:
#         ans += row.count(0)
#     if ans > max_safe:
#         max_safe = ans

# print(max_safe)
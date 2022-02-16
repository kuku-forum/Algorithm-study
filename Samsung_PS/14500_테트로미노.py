import sys

N, M = map(int, sys.stdin.readline().split())

board_lst = []
answer = 0

for _ in range(N):
    board_lst.append(list(map(int, sys.stdin.readline().split())))

tetmino_dic = {
            0: [[1, 1, 1, 1]],
            
            1: [[1,1], 
                [1,1]],
            
            2: [[1,0], 
                [1,0], 
                [1,1]],
            
            3: [[1,0], 
                [1,1], 
                [0,1]],
            
            4: [[1,1,1], 
                [0,1,0]]
}

def rotate90(arr):
    return list(zip(*reversed(arr)))


def symmetry(arr):
    return [list(reversed(a)) for a in arr]


def conv(arr):
    global answer
    tmp = 0
    for s_i in range(N - len(arr) + 1):
        for s_j in range(M - len(arr[0]) + 1):
            
            for i in range(len(arr)):
                for j in range(len(arr[0])):                    
                    tmp += arr[i][j] * board_lst[s_i + i][s_j + j]
            if tmp > answer:
                answer = tmp
            tmp = 0
    
    
for i in range(5):
    tetmino = tetmino_dic[i]

    # rot90 한번
    if i == 0:
        conv(tetmino)
        conv(rotate90(tetmino))
    
    # 정사각형은 상관없음
    elif i == 1:
        conv(tetmino)

    # rot90 4번, 대칭 후 rot90 4번의 경우 존재
    elif i == 2 :
        
        for _ in range(4):
            tetmino = rotate90(tetmino)
            conv(tetmino)
        
        tetmino = symmetry(tetmino)
        for _ in range(4):
            tetmino = rotate90(tetmino)
            conv(tetmino)

    # rot90, 대칭, 대칭 후 rot90
    elif i == 3:
        conv(tetmino)
        conv(rotate90(tetmino))
        tetmino = symmetry(tetmino)
        conv(tetmino)
        conv(rotate90(tetmino))

    elif i == 4:
        # 4 가지 회전할 경우
        for _ in range(4):
            tetmino = rotate90(tetmino)
            conv(tetmino)

print(answer)



###################################################################################

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 모든 유형의 테트로미노를 탐색하도록 함
def dfs(r, c, idx, total): # idx는 칸의 수, total은 칸에 쓰인 수들의 합
    global ans
    
    # 가지치기
    # 남은 idx가 max_val 만큼 있어도, ans 보다 작으면 끝내버림
    if ans >= total + max_val * (3 - idx):
        return
    
    # 4(0, 1, 2, 3)개의 정사각형을 탐색했으면 리턴
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        # 총 4번 움직임
        for i in range(4):
            # 상하좌우
            nr = r + dr[i]
            nc = c + dc[i]

            # board 안 벗어나고, 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                
                # 2번째(0, 1, 2, 3) idx에서 ㅗ ㅓ ㅏ ㅜ 를 위해 실행
                # 기존 r, c로  index 변환
                if idx == 1:
                    visited[nr][nc] = 1
                    # 새로 방문한 곳이 아닌, 원래 위치에서 dfs 진행
                    # total값에 새로 도착한 board 값 추가
                    dfs(r, c, idx+1, total + board[nr][nc])
                    visited[nr][nc] = 0
                
                # 새로 도착한 좌표에서 dfs 실행
                # total값에 새로 도착한 board 값 추가
                visited[nr][nc] = 1
                dfs(nr, nc, idx + 1, total + board[nr][nc])
                visited[nr][nc] = 0


N, M = map(int, input().split()) # N: 세로크기, M: 가로크기
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

ans = 0
# 모든 보드값에서 가장 큰 수
max_val = max(map(max, board))


# board의 모든 영역 dfs 탐색
for i in range(N):
    for j in range(M):
        
        # 방문처리
        visited[i][j] = 1
        
        # 행, 열, idx, board의 값이 들어감
        # ex) 0,0 에서 어떤 도형의 값이 가장 큰지 확인
        dfs(i, j, 0, board[i][j])
        
        # 방문처리 해제
        visited[i][j] = 0

print(ans)
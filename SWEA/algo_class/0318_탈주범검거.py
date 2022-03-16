from my_package.hjtc import swea_tc 

def print_board(arr):
    for row in arr:
        print(row)
    print()

from collections import deque

tunnel_dic = {
    1: [1, 1, 1, 1],
    2: [1, 0, 1, 0],
    3: [0, 1, 0, 1],
    4: [1, 1, 0, 0],
    5: [0, 1, 1, 0],
    6: [0, 0, 1, 1],
    7: [1, 0, 0, 1],
}

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for t in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[R][C] = 1
    
    que = deque([[R, C]])    
    answer = 0
    for _ in range(L - 1):
        
        answer += len(que)
        for _ in range(len(que)):
            r, c = que.popleft()
            
            for i, (dr, dc) in enumerate(directions):
                nr = r + dr
                nc = c + dc
                
                if N > nr >= 0 and M > nc >= 0 and visited[nr][nc] == 0 and board[nr][nc] > 0:
                    if tunnel_dic[board[r][c]][i] == 1 and tunnel_dic[board[nr][nc]][(i+2)%4] == 1:
                        visited[nr][nc] = 1
                        que.append([nr, nc])
    answer += len(que)
    print_board(visited)
    print(f'#{t} {answer}')
    if t == 2:
        break
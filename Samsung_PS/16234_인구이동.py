from collections import deque

N, L, R = map(int, input().split())
board_lst = []

for _ in range(N):
    board_lst.append(list(map(int, input().split())))

def bfs(y, x, used, board):
    global is_move
    direction_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    que = deque([[y, x]])
    used[y][x] = 1
    cnt = 1
    union = [[y, x]]
    person = board[y][x]

    while que:
        y, x = que.popleft()

        for direct in direction_lst:
            ny, nx = y + direct[0], x + direct[1]

            if N > ny >= 0 and N > nx >= 0 and used[ny][nx] == 0:
                if R >= abs(board[ny][nx] - board[y][x]) >= L:
                    used[ny][nx] = 1
                    que.append([ny, nx])

                    union.append([ny, nx])
                    person += board[ny][nx]
                    cnt += 1
    if cnt > 1:
        is_move = True
        mean = person//cnt
        for i, j in union:
            board[i][j] = mean


# 정답
answer = 0
while True:
    is_move = False
    used = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if used[i][j] == 1:
                continue
            bfs(i, j, used, board_lst)

    if is_move:
        answer += 1
    else:
        break

print(answer)
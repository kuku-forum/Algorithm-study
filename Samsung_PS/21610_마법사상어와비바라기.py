N, M = map(int, input().split())
board = []
command = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for _ in range(M):
    command.append(list(map(int, input().split())))

direction = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
position = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
visited = [[False for _ in range(N)] for _ in range(N)]


def cloud(pos, dirc, stance):
    for i in range(len(pos)):
        ny = (pos[i][0] + dirc[0] * stance)%N
        nx = (pos[i][1] + dirc[1] * stance)%N

        pos[i][0] = ny
        pos[i][1] = nx
        board[ny][nx] += 1
        visited[ny][nx] = True

    return pos


def water_copy(pos):
    diagnol = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

    for y, x in pos:
        cnt = 0
        for dig in diagnol:
            ny = y + dig[0]
            nx = x + dig[1]

            if N > ny >= 0 and N > nx >= 0:
                if board[ny][nx] > 0:
                    cnt += 1
        board[y][x] += cnt


def rever_cloud():
    new_cloud = []
    for i in range(N):
        for j in range(N):

            if not visited[i][j]:
                if board[i][j] >= 2:
                    board[i][j] -= 2
                    new_cloud.append([i, j])
                    visited[i][j] = True
            else:
                visited[i][j] = False

    return new_cloud


for cmd in command:
    d, s = cmd[0], cmd[1]
    position = cloud(position, direction[d], s)
    water_copy(position)
    position = rever_cloud()
    visited = [[False for _ in range(N)] for _ in range(N)]
    #
    # print('#2', visited)
    # print(position)
    # print(board)
    # print()

answer = 0

for row in board:
    answer += sum(row)

print(answer)
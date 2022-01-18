N, Q = map(int, input().split())

board_lst = []
width = 2**N
for _ in range(width):
    board_lst.append(list(map(int, input().split())))

L_lst = list(map(int, input().split()))

def rot90(board, expo):
    cut = 2**expo
    cut_board = [[[i, j] for j in range(cut)] for i in range(cut)]
    rot_board = []

    for row in zip(*cut_board):
        tmp = list(reversed(row))
        rot_board.append(tmp)

    standard_lst = [[i, j] for i in range(0, width, cut) for j in range(0, width, cut)]

    for standard in standard_lst:
        val_lst = []
        for row in rot_board:
            for pos in row:
                ny = standard[0] + pos[0]
                nx = standard[1] + pos[1]
                val_lst.append(board[ny][nx])
        idx = 0
        for row in cut_board:
            for pos in row:
                ny = standard[0] + pos[0]
                nx = standard[1] + pos[1]
                # print(ny, nx, idx, val_lst)
                board[ny][nx] = val_lst[idx]
                idx += 1
    return board


def fireball(board):
    direct_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    target_lst = []
    for y in range(width):
        for x in range(width):
            cnt = 0
            for direct in direct_lst:
                ny = y + direct[0]
                nx = x + direct[1]

                if width > ny >= 0 and width > nx >= 0:
                    if board[ny][nx] > 0:
                        cnt += 1

            if 2 >= cnt:
                target_lst.append([y, x])

    for target in target_lst:
        y = target[0]
        x = target[1]

        if board[y][x] == 0:
            continue
        else:
            board[y][x] -= 1
    return


def dfs(board):
    visited = [[0 for _ in range(width)] for _ in range(width)]
    direct_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    num = 0

    for i in range(width):
        for j in range(width):
            if visited[i][j] == 1 or board[i][j] == 0:
                continue
            root = []
            root.append([i, j])
            cnt = 0

            while root:
                # print(root)
                y, x = root.pop()
                # print(y, x)

                for direct in direct_lst:
                    ny = y + direct[0]
                    nx = x + direct[1]

                    if width > ny >= 0 and width > nx >= 0 and visited[ny][nx] == 0 and board[ny][nx] > 0:
                        visited[ny][nx] = 1
                        root.append([ny, nx])
                        cnt += 1

            num = max(num, cnt)

    return num


for L in L_lst:
    rot90(board_lst, L)
    fireball(board_lst)


# for row in board_lst:
#     print(row)
# print()

answer = 0
for row in board_lst:
    answer += sum(row)
print(answer)

bound = dfs(board_lst)
print(bound)









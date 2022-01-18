from collections import deque

N = int(input())

board_lst = []
root = []
direction_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    row = []
    for j, factor in enumerate(map(int, input().split())):
        if factor == 9:
            root = [i, j]
            row.append(0)
            continue
        row.append(factor)
    board_lst.append(row)


def print_board(arr):
    for row in arr:
        print(row)
    return

# print_board(board_lst)


def bfs(board, root):
    que = deque([root])
    used = [[-1 for _ in range(N)] for _ in range(N)]
    used[root[0]][root[1]] = 0
    board[root[0]][root[1]] = 0
    size = 2
    cnt = 0
    full = 0

    while que:
        catch = []
        routine = len(que)
        for _ in range(routine):
            y, x = que.popleft()

            for direct in direction_lst:
                ny, nx = y + direct[0], x + direct[1]
                if N > ny >= 0 and N > nx >= 0 and used[ny][nx] == -1 and size >= board[ny][nx]:
                    used[ny][nx] = used[y][x] + 1
                    que.append([ny, nx])
                    if size > board[ny][nx] > 0:
                        catch.append([used[y][x] + 1, ny, nx])

        if catch:
            # print('catch',cnt, used[y][x] + 1, size, catch)
            catch.sort(key=lambda x: (x[0], x[1], x[2]))
            dist, cy, cx = catch[0]
            # print(cy, cx, dist)
            cnt += dist
            full += 1
            if full == size:
                size += 1
                full = 0

            used = [[-1 for _ in range(N)] for _ in range(N)]
            used[cy][cx] = 0
            board[cy][cx] = 0

            que = deque([[cy, cx]])
        elif not que:
            break

    return cnt


answer = bfs(board_lst, root)
print(answer)
import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
volume, root_list = [], []

for z in range(H):
    space = []
    for y in range(N):
        line = []
        for x, num in enumerate(map(int, sys.stdin.readline().split())):
            if num == 1:
                root_list.append([z, y, x])
            line.append(num)
        space.append(line)
    volume.append(space)

def tomato_3d(board, root):
    direct_list = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
    que = deque(root)
    day = -1

    while que:
        day += 1

        for _ in range(len(que)):
            z, y, x = que.popleft()

            for direct in direct_list:
                n_z = z + direct[0]
                n_y = y + direct[1]
                n_x = x + direct[2]

                if H > n_z >= 0 and N > n_y >= 0 and M > n_x >= 0 and board[n_z][n_y][n_x] == 0:
                    board[n_z][n_y][n_x] = board[z][y][x] + 1
                    que.append([n_z, n_y, n_x])

    for space in board:
        for line in space:
            if 0 in line:
                return -1
    return day

print(tomato_3d(volume, root_list))

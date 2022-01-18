import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
board_list, root_list = [], []
direct_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for y in range(N):
    tmp = []
    for x, num in enumerate(map(int, sys.stdin.readline().split())):
        if num == 1:
            root_list.append([y, x])
        tmp.append(num)
    board_list.append(tmp)

def tomato(board, root):
    que = deque(root)
    day = -1

    while que:
        day += 1

        for _ in range(len(que)):
            y, x = que.popleft()

            for direct in direct_list:
                n_y = y + direct[0]
                n_x = x + direct[1]

                if N > n_y >= 0 and M > n_x >= 0 and board[n_y][n_x] == 0:
                    board[n_y][n_x] = board[y][x] + 1
                    que.append([n_y, n_x])
    
    for row in board:
        if 0 in row:
            return -1
    return day

print(tomato(board_list, root_list))
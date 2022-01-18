import sys
from collections import deque

N, M, x, y, K = map(int, sys.stdin.readline().split())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

com_lst = list(map(int, sys.stdin.readline().split()))

# 동 서 남 북
dir_dic = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}

dice_col = deque([0, 0, 0, 0])
dice_row = deque([0, 0, 0])

dice = deque([[0, 2, 0],
              [4, 1, 3]
              [0, 5, 0]
              [0, 6, 0]])

'''
  2      1
4 1 3  4 5 <- dice_col[1] 6
  5      6
  6      2 <- dice_col[3]
'''
answer = []

for com in com_lst:
    x += dir_dic[com][0]
    y += dir_dic[com][1]

    if N > x >= 0 and M > y >= 0:
        if com == 1: 
            dice_row.rotate(1) # 동
            
        elif com == 2: # 서
            dice_row.rotate(-1)
        elif com == 3: # 남
            dice_col.rotate(1)
        elif com == 4: # 북
            dice_col.rotate(-1)
            if board[x][y] == 0:
                board[x][y] = dice_row[0]
            else:
                dice_row[0] = board[x][y]
                board[x][y] = 0
            answer.append(dice_row[2])






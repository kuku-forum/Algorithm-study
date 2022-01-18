'''
등장 횟수가 커지는 순으로,
그러한 것이 여러가지면 수가 커지는 순으
'''

from collections import defaultdict

R, C, K = map(int, input().split())

board_lst = []

for _ in range(3):
    board_lst.append(list(map(int, input().split())))


def solution(board):

    for cnt in range(101):
        if len(board) > R-1 >= 0 and len(board[0]) > C-1 >= 0 and board[R-1][C-1] == K:
            # for row in board:
            #     print(row)
            return cnt

        if len(board) >= len(board[0]):
            tmp_board = []
            for i in range(len(board)):
                arr = defaultdict(int)
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        continue
                    arr[board[i][j]] += 1
                # print(arr)
                row = sorted(arr, key=lambda x: (arr[x], x))

                tmp_row = []
                for r in row:
                    # if r == 0:
                    #     continue
                    tmp_row.append(r)
                    tmp_row.append(arr[r])
                tmp_board.append(tmp_row)

            w = len(max(tmp_board, key=lambda x: len(x)))
            h = len(tmp_board)
            tmp_board_pad = [[0 for _ in range(w)] for _ in range(h)]

            for i in range(len(tmp_board)):
                for j in range(len(tmp_board[i])):
                    tmp_board_pad[i][j] = tmp_board[i][j]

            board = tmp_board_pad

        else:
            tmp_board = []
            for j in range(len(board[0])):
                arr = defaultdict(int)
                for i in range(len(board)):
                    if board[i][j] == 0:
                        continue
                    arr[board[i][j]] += 1

                col = sorted(arr, key=lambda x: (arr[x], x))
                tmp_col = []
                for c in col:
                    # if c == 0:
                    #     continue
                    tmp_col.append(c)
                    tmp_col.append(arr[c])
                tmp_board.append(tmp_col)

            w = len(tmp_board)
            h = len(max(tmp_board, key=lambda x: len(x)))
            tmp_board_trans = [[0 for _ in range(w)] for _ in range(h)]

            for i in range(len(tmp_board)):
                for j in range(len(tmp_board[i])):
                    tmp_board_trans[j][i] = tmp_board[i][j]

            board = tmp_board_trans

    return -1


answer = solution(board_lst)
print(answer)


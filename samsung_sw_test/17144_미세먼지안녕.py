from collections import defaultdict

R, C, T = map(int, input().split())

air_loc = []
board_lst = []
direction_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(R):
    row = []
    for j, factor in enumerate(map(int, input().split())):
        if factor == -1:
            air_loc.append([i, j])
        row.append(factor)
    board_lst.append(row)


def diffuse(board):
    used = [[[] for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):

            total_dust = board[r][c]
            if total_dust == -1:
                used[r][c].append(-1)
                continue
            dif_dust = total_dust//5

            for direct in direction_lst:
                nr = r + direct[0]
                nc = c + direct[1]

                if R > nr >= 0 and C > nc >= 0 and board[nr][nc] != -1:
                    used[nr][nc].append(dif_dust)
                    total_dust -= dif_dust

            used[r][c].append(total_dust)

    for r in range(R):
        for c in range(C):
            board[r][c] = sum(used[r][c])

    return board

def operation(board, air):
    op_lst_1 = []
    op_lst_2 = []
    air_1 = air[0]
    air_2 = air[1]

    for c in range(1, C):
        op_lst_1.append([air_1[0], c])
    for r in range(air_1[0]-1, 0, -1):
        op_lst_1.append([r, C-1])
    for c in range(C-1, -1, -1):
        op_lst_1.append([0, c])
    for r in range(1, air_1[0] + 1):
        op_lst_1.append([r, 0])

    for c in range(1, C):
        op_lst_2.append([air_2[0], c])
    for r in range(air_2[0] + 1, R):
        op_lst_2.append([r, C-1])
    for c in range(C-2, 0, -1):
        op_lst_2.append([R-1, c])
    for r in range(R-1, air_2[0]-1, -1):
        op_lst_2.append([r, 0])

    op_dic_1 = defaultdict(int)
    op_dic_2 = defaultdict(int)
    for i in range(len(op_lst_1)):
        pre = op_lst_1[i-1]
        cur = op_lst_1[i]
        if board[pre[0]][pre[1]] == -1:
            op_dic_1[cur[0], cur[1]] = 0
        else:
            op_dic_1[cur[0], cur[1]] = board[pre[0]][pre[1]]

    for i in range(len(op_lst_2)):
        pre = op_lst_2[i-1]
        cur = op_lst_2[i]
        if board[pre[0]][pre[1]] == -1:
            op_dic_2[cur[0], cur[1]] = 0
        else:
            op_dic_2[cur[0], cur[1]] = board[pre[0]][pre[1]]

    for pos in op_dic_1:
        if pos[0] == air_1[0] and pos[1] == air_1[1]:
            continue
        board[pos[0]][pos[1]] = op_dic_1[pos]

    for pos in op_dic_2:
        if pos[0] == air_2[0] and pos[1] == air_2[1]:
            continue
        board[pos[0]][pos[1]] = op_dic_2[pos]

    return board


for _ in range(T):
    board_lst = diffuse(board_lst)
    board_lst = operation(board_lst, air_loc)

answer = 0
for row in board_lst:
    answer += sum(row)
print(answer + 2)


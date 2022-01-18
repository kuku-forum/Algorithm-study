from collections import defaultdict

board_lst = defaultdict(list)
pos_lst = defaultdict(list)
answer = 0

for i in range(4):
    info = list(map(int, input().split()))
    for j in range(0, len(info), 2):
        if i == 0 and j == 0:
            answer += info[j]
            board_lst['M'] = [i, j // 2, info[j+1]]
            pos_lst[(i, j//2)] = ['M', info[j+1]]
            continue

        board_lst[info[j]] = [i, j//2, info[j+1]]
        pos_lst[(i, j // 2)] = [info[j], info[j + 1]]

print(board_lst)
print(pos_lst)
direct_lst = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def move_fish(board):

    for i in range(1, 17):
        if not board[i]:
            continue

        y = board[i][0]
        x = board[i][1]
        # print(board[i])
        direct = direct_lst[board[i][2]-1]

        ny = y + direct[0]
        nx = x + direct[1]

        if 4 > ny >= 0 and 4 > nx >= 0:
            fish_name_1, fish_direct_1 = pos_lst[(y, x)]

            # fish_name_2 = pos_lst[(ny, nx)][0]

            if fish_name_1 == 'M':
                for _ in range(8):
                    fish_direct_1 = (fish_direct_1+1)//8
                    run_direct = direct_lst[fish_direct_1]

                    ny = y + run_direct[0]
                    nx = x + run_direct[1]

                    if 4 > ny >= 0 and 4 > nx >= 0:
                        if not pos_lst[(ny, nx)]:
                            fish_name_2, fish_pos_2 = pos_lst[(ny, nx)]

                            pos_lst[(ny, nx)] = [fish_name_1, fish_direct_1]
                            pos_lst[(y, x)] = []

                            board[fish_name_1] = [ny, nx, fish_direct_1]
                            board[fish_name_2] = []

    return

move_fish((board_lst))
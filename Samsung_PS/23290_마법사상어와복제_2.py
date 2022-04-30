from copy import deepcopy

def print_board(arr):
    for row in arr:
        print(row)
    print()

def permutation(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        tmp = [arr[i]]
        for e in permutation(arr, n-1):
            result.append(tmp + e)

    return result


M, S = map(int, input().split())

board = [[[] for _ in range(4)] for _ in range(4)]

for _ in range(M):
    fr, fc, fd = map(int, input().split())
    fr -= 1
    fc -= 1
    fd -= 1
    board[fr][fc].append(fd)

sr, sc = map(int, input().split())
sr -= 1
sc -= 1

scent_board = [[0 for _ in range(4)] for _ in range(4)]

fish_directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
                   (0, 1), (1, 1), (1, 0), (1, -1)]

s_case = permutation(['1', '2', '3', '4'], 3)
# print(s_case)
# print(len(s_case))
s_directions = {1: [-1, 0],
                2: [0, -1],
                3: [1, 0],
                4: [0, 1]}


def fish_copy(pre_board, cur_board):
    for r in range(4):
        for c in range(4):
            cur_board[r][c].extend(pre_board[r][c])

    return cur_board

def fish_move(board):
    n_board = [[[] for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            while board[r][c]:
                d = board[r][c].pop()
                for dd in range(8):
                    nd = (d - dd)%8

                    dr, dc = fish_directions[nd]
                    nr = r + dr
                    nc = c + dc

                    if 4 > nr >= 0 and 4 > nc >= 0 and scent_board[nr][nc] == 0 and (sr, sc) != (nr, nc):
                        n_board[nr][nc].append(nd)
                        # print_board(board)
                        break
                else:
                    board[r][c].append(d)
                    n_board[r][c].extend(board[r][c])
                    # n_board[r][c] = board[r][c]
                    break
    return n_board


def shark_move(sr, sc):
    possible_case = []

    for step_lst in s_case:
        tmp = ''
        nsr, nsc = sr, sc
        tmp_case = set()

        for step in step_lst:
            tmp += step
            dsr, dsc = s_directions[int(step)]
            nsr += dsr
            nsc += dsc
            if 4 > nsr >= 0 and 4 > nsc >= 0:
                tmp_case.add((nsr, nsc))
            else:
                break
        else:
            kill_num = 0
            for cr, cc in tmp_case:
                kill_num += len(board[cr][cc])
            possible_case.append([int(tmp), kill_num, tmp_case])

    possible_case.sort(key=lambda x: (-x[1], x[0]))
    # print(possible_case)


    for step in str(possible_case[0][0]):
        # print(step)
        dsr, dsc = s_directions[int(step)]
        sr += dsr
        sc += dsc

        if board[sr][sc]:
            board[sr][sc] = []
            scent_board[sr][sc] = 3

    return sr, sc


def scent_diffuse():
    for r in range(4):
        for c in range(4):
            if scent_board[r][c] > 0:
                scent_board[r][c] -= 1



for _ in range(S):
    pre_board = deepcopy(board)
    # print_board(board)

    board = fish_move(board)
    # print_board(board)
    # print(sr, sc)
    sr, sc = shark_move(sr, sc)
    # print_board(board)

    scent_diffuse()

    board = fish_copy(pre_board, board)

    # print('#'*10)

# print(sr, sc)
# print_board(board)
answer = 0
for r in range(4):
    for c in range(4):
        answer += len(board[r][c])

print(answer)





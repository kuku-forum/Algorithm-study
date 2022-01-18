from collections import defaultdict
from copy import deepcopy

N, M = map(int, input().split())

board_lst = []

for _ in range(N):
    board_lst.append(list(map(int, input().split())))

direct_lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]

x_dic = defaultdict(list)
answer = 0

def dfs(board, root):
    
    point = [root]
    color = board[root[0]][root[1]]
    candi_tmp = []
    rainbow = 0

    if color == -1 or color == 'x' or color == 0:
        return

    while point:
        y, x = point.pop()   
        for dir in direct_lst:
            ny = y + dir[0]
            nx = x + dir[1]
            if N > ny >= 0 and N > nx >= 0:
                if board[ny][nx] == 0 or color == board[ny][nx]:
                    if board[ny][nx] == 0:
                        rainbow += 1
                    candi_tmp.append((ny, nx))
                    point.append((ny, nx))
                    board[ny][nx] = 'x'
    else:
        if len(candi_tmp) >= 2:
            candi_tmp.sort(key = lambda x: (x[0], x[1]))
            candidate[color].append((rainbow, candi_tmp[0][0], candi_tmp[0][1]))
            x_dic[(rainbow, candi_tmp[0][0], candi_tmp[0][1])] = candi_tmp
    return


def rotate90(arr):
    arr2 = list(map(list, zip(*arr)))
    arr2.reverse()
    return arr2

def gravity(board):
    for j in range(N):
        i = N-1
        while True:
        
            if 0 >= i:
                break

            if board[i][j] == 'x':
                for y in range(i-1, -1, -1):
                    if board[y][j] == -1:
                        i -= 1
                        break

                    elif board[y][j] == 'x':
                        continue
                    else:
                        board[i][j] = board[y][j]
                        board[y][j] = 'x'
                        i -= 1
                else:
                    i -= 1
            else:
                i -= 1


def make_group():
    score = 0
    for i in range(N):
        for j in range(N):
            dfs(deepcopy(board_lst), (i, j))

    for candi in reversed(candidate):
        if not candi:
            continue
        candi.sort(key=lambda x: (-x[0], -x[1], -x[2]))
        score += len(x_dic[candi[0]])**2
        break
    if not candi:
        return score

    for y, x in x_dic[candi[0]]:
        board_lst[y][x] = 'x'

    return score


while True:
    candidate = [[] for _ in range(M+1)]

    score = make_group()
    # print('#1', board_lst)
    # print(score)
    answer += score


    gravity(board_lst)
    # print('#2', board_lst)
    board_lst = rotate90(board_lst)
    # print('#3', board_lst)
    gravity(board_lst)
    # print('#4', board_lst)
    # print()

    if score == 0:
        break
print(answer)



'''


'''
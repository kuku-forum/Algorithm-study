from pprint import pprint
from collections import deque
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
com_lst = [list(map(int, input().split())) for _ in range(M)]

# pprint(board)
# pprint(com_lst)
cr = cc = N//2
skill_dic = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
bead_lst = deque([])
exp_bead = {1: 0, 2: 0, 3: 0}


def make_bead_lst(sr, sc):
    d = term = 0
    cnt = 1
    while True:
        term += 1
        for _ in range(2):
            d += 1
            dr, dc = directions[(d-1)%4]
            for _ in range(term):
                sr += dr
                sc += dc

                if N > sr >= 0 and N > sc >= 0:
                    bead_lst.append(board[sr][sc])
                    board[sr][sc] = cnt
                    cnt += 1
                else:
                    return


def blizzard(d, s):
    nr, nc = cr, cc
    for _ in range(s):
        nr += skill_dic[d][0]
        nc += skill_dic[d][1]

        if len(bead_lst) > board[nr][nc]-1:
            bead_lst[board[nr][nc]-1] = 0
    return


def move_bead(que):
    new_que = deque([])
    # flag = False

    while que:
        node = que.popleft()
        if node > 0:
            new_que.append(node)
        # else:
        #     flag = True

    return new_que


def explosion(que):
    new_que = deque([])
    buffer = deque([])
    flag = False

    while que:
        if not buffer:
            buffer.append(que.popleft())
            continue

        if buffer[-1] == que[0]:
            buffer.append(que.popleft())
        else:
            if 4 > len(buffer):
                new_que.extend(buffer)
            else:
                flag = True
                for node in buffer:
                    exp_bead[node] += 1
            buffer = deque([])

    if 4 > len(buffer):
        new_que.extend(buffer)
    else:
        flag = True
        for node in buffer:
            exp_bead[node] += 1

    return flag, new_que


def transfer_bead(que):
    new_que = deque([])
    buffer = deque([])

    while que:
        if not buffer:
            buffer.append(que.popleft())
            continue

        if buffer[-1] == que[0]:
            buffer.append(que.popleft())
        else:
            new_que.append(len(buffer))
            if len(new_que) == bound:
                return new_que
            new_que.append(buffer[0])
            if len(new_que) == bound:
                return new_que
            buffer = deque([])

    if buffer:
        new_que.append(len(buffer))
        if len(new_que) == bound:
            return new_que
        new_que.append(buffer[0])
        if len(new_que) == bound:
            return new_que
    return new_que


make_bead_lst(cr, cc)
bound = N**2 - 1

for com in com_lst:
    blizzard(*com)
    # print(bead_lst, len(bead_lst))
    # print('###')
    gogo = True
    bead_lst = move_bead(bead_lst)
    # print('m', bead_lst, len(bead_lst))
    if not bead_lst: break
    while gogo:
        gogo, bead_lst = explosion(bead_lst)
        if not bead_lst: break
    #     print('b', bead_lst, len(bead_lst))
    # print('###')

    bead_lst = transfer_bead(bead_lst)
    # print(bead_lst, len(bead_lst))
    # break

# print(bead_lst)
# print(exp_bead)
answer = exp_bead[1] + 2*exp_bead[2] + 3*exp_bead[3]
print(answer)

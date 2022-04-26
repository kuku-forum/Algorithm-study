from pprint import pprint
from collections import deque


machine_lst = []
chk_lst = []
wall_lst = []
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
wall_dic = {}
answer = 0

R, C, K = map(int, input().split())

for i in range(R):
    for j, e in enumerate(map(int, input().split())):
        if 5 > e > 0:
            machine_lst.append((i, j, e))
        elif e == 5:
            chk_lst.append((i, j))

for _ in range(int(input())):
    wall_lst.append(list(map(int, input().split())))

for i in range(len(wall_lst)):
    wall_lst[i][0] -= 1
    wall_lst[i][1] -= 1

for r, c, t in wall_lst:
    if t == 0:
        wall_dic[(r, c, r-1, c)] = 1
        wall_dic[(r-1, c, r, c)] = 1
    else:
        wall_dic[(r, c, r, c+1)] = 1
        wall_dic[(r, c+1, r, c)] = 1

env_map = [[0 for _ in range(C)] for _ in range(R)]


def outline_func(board):
    for r in range(R):
        if board[r][0] > 0:
            board[r][0] -= 1

        if board[r][-1] > 0:
            board[r][-1] -= 1

    for c in range(1, C-1):
        if board[0][c] > 0:
            board[0][c] -= 1

        if board[-1][c] > 0:
            board[-1][c] -= 1


def finish_chk():
    for r, c in chk_lst:
        if K > env_map[r][c]:
            return True
    return False


def temp_control():
    venv_map = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(R):
        for c in range(C):
            cur_temp = env_map[r][c]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if R > nr >= 0 and C > nc >= 0 and not wall_dic.get((r, c, nr, nc)):
                    next_temp = env_map[nr][nc]

                    if cur_temp > next_temp:
                        d_temp = (cur_temp - next_temp) // 4
                        venv_map[nr][nc] += d_temp
                        venv_map[r][c] -= d_temp

    for r in range(R):
        for c in range(C):
            env_map[r][c] += venv_map[r][c]

heat_dic = {
    1: [[[-1, 0], [-1, 1]],
        [[0, 1]],
        [[1, 0], [1, 1]]],

    2: [[[-1, 0], [-1, -1]],
        [[0, -1]],
        [[1, 0], [1, -1]]],

    3: [[[0, 1], [-1, 1]],
        [[-1, 0]],
        [[0, -1], [-1, -1]]],

    4: [[[0, -1], [1, -1]],
        [[1, 0]],
        [[0, 1], [1, 1]]],
}


def heat_func():
    for r, c, m in machine_lst:
        dr, dc = directions[m-1]
        sr = r + dr
        sc = c + dc
        heat = 5
        heat_map = [[0 for _ in range(C)] for _ in range(R)]

        if R > sr >= 0 and C > sc >= 0 and not wall_dic.get((r, c, sr, sc)):
            visited = [[0 for _ in range(C)] for _ in range(R)]
            que = deque([])
            heat_map[sr][sc] += heat
            env_map[sr][sc] += heat
            visited[sr][sc] = 1
            que.append([sr, sc])

            while que:
                ssr, ssc = que.popleft()
                for i in range(3):

                    if i == 1:
                        sdr, sdc = heat_dic[m][i][0]
                        nr = ssr + sdr
                        nc = ssc + sdc

                        if R > nr >= 0 and C > nc >= 0:
                            if not wall_dic.get((ssr, ssc, nr, nc)) and visited[nr][nc] == 0 and heat_map[ssr][ssc] > 1:
                                heat_map[nr][nc] += heat_map[ssr][ssc]-1
                                env_map[nr][nc] += heat_map[ssr][ssc] - 1
                                visited[nr][nc] = 1
                                que.append([nr, nc])

                    else:
                        sdr1, sdc1 = heat_dic[m][i][0]
                        sdr2, sdc2 = heat_dic[m][i][1]

                        nr1 = ssr + sdr1
                        nc1 = ssc + sdc1

                        nr2 = ssr + sdr2
                        nc2 = ssc + sdc2

                        if R > nr1 >= 0 and C > nc1 >= 0 and not wall_dic.get((ssr, ssc, nr1, nc1)):
                            if R > nr2 >= 0 and C > nc2 >= 0 and not wall_dic.get((nr1, nc1, nr2, nc2)):
                                if visited[nr2][nc2] == 0 and heat_map[ssr][ssc] > 1:
                                    heat_map[nr2][nc2] += heat_map[ssr][ssc]-1
                                    env_map[nr2][nc2] += heat_map[ssr][ssc]-1
                                    visited[nr2][nc2] = 1
                                    que.append([nr2, nc2])
    return

flag = True

while flag:
    if answer > 100:
        break

    heat_func()
    temp_control()
    outline_func(env_map)
    answer += 1
    flag = finish_chk()

print(answer)







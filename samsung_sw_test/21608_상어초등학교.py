from collections import defaultdict

N = int(input())

students = defaultdict(list)
board = [[0 for _ in range(N)] for _ in range(N)]
score = [0, 1, 10, 100, 1000]
direction_lst = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0
for _ in range(N ** 2):
    tmp = list(map(int, input().split()))
    students[tmp[0]] = [i for i in tmp[1:]]


def func_1(std, favor):
    global answer
    candi_lst = [[] for _ in range(5)]

    for i in range(N):
        for j in range(N):

            if board[i][j] != 0:
                continue
            cnt = 0
            empty = 0

            for dirc in direction_lst:
                r = dirc[0] + i
                c = dirc[1] + j

                if N > r >= 0 and N > c >= 0:
                    if board[r][c] in favor:
                        cnt += 1
                    elif board[r][c] == 0:
                        empty += 1
            candi_lst[cnt].append((i, j, empty))
    # print()
    # print(board)
    # print(candi_lst)
    for candi in reversed(candi_lst):
        if candi:
            # print(candi)

            if len(candi) == 1:
                board[candi[0][0]][candi[0][1]] = std
            else:
                candi.sort(key=lambda x: (-x[2], x[0], x[1]))
                # print(candi)
                board[candi[0][0]][candi[0][1]] = std
            return


for student in students:
    favorite_lst = students[student]
    func_1(student, favorite_lst)

for i in range(N):
    for j in range(N):
        cnt = 0
        favorite_lst = students[board[i][j]]

        for dirc in direction_lst:
            r = dirc[0] + i
            c = dirc[1] + j

            if N > r >= 0 and N > c >= 0:
                if board[r][c] in favorite_lst:
                    cnt += 1
        # print(board[i][j], cnt)

        answer += score[cnt]

print(answer)

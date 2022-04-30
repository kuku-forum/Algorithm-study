from pprint import pprint
def print_board(arr):
    for row in arr:
        print(row)
    print()


N = int(input())

stu_lst = []
stu_dic = {}
for _ in range(N**2):
    s, *info = map(int, input().split())
    stu_dic[s] = info
    stu_lst.append([s, info])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
board = [[0 for _ in range(N)] for _ in range(N)]


for stu_info in stu_lst:
    stu = stu_info[0]
    fav_lst = stu_info[1]
    seat_candi = []

    for r in range(N):
        for c in range(N):
            fav_cnt = emp_cnt = 0
            if board[r][c] != 0:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if N > nr >= 0 and N > nc >= 0:
                    if board[nr][nc] == 0:
                        emp_cnt += 1
                    elif board[nr][nc] in fav_lst:
                        fav_cnt += 1
            seat_candi.append([fav_cnt, emp_cnt, r, c])

    seat_candi.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    # print(seat_candi)
    _, _, sr, sc = seat_candi[0]
    board[sr][sc] = stu

# print_board(board)

answer = 0


for r in range(N):
    for c in range(N):
        stu = board[r][c]
        fav_lst = stu_dic[stu]
        fav_cnt = 0

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if N > nr >= 0 and N > nc >= 0:
                if board[nr][nc] in fav_lst:
                    fav_cnt += 1

        if fav_cnt == 1:
            answer += 1
        elif fav_cnt == 2:
            answer += 10
        elif fav_cnt == 3:
            answer += 100
        elif fav_cnt == 4:
            answer += 1000

print(answer)
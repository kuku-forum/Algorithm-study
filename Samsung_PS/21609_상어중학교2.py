def print_board(arr):
    for row in arr:
        print(row)
    print()

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def rot270(arr):
    return list(map(list, zip(*arr)))[::-1]

#
# def gravity():
#     for c in range(N):
#         base_point = None
#         for r in range(N-1, -1, -1):
#             if board[r][c] == -2:
#                 base_point = r
#                 break
#         else:
#             continue
#
#         nr = base_point-1
#         while N > nr >= 0:
#             if board[nr][c] == -2:
#                 if base_point == None:
#                     base_point = nr
#                 nr -= 1
#
#             elif board[nr][c] == -1:
#                 if base_point != None:
#                     base_point = None
#                 nr -= 1
#
#             elif board[nr][c] >= 0:
#                 if base_point != None:
#                     board[base_point][c], board[nr][c] = board[nr][c], -2
#                     # for bpr in range(base_point, -1, -1):
#                     #     if board[bpr][c] == -2:
#                     #         base_point = r
#                 nr -= 1

# def gravity(board):
#     N = len(board)
#
#     for x in range(N):
#         y = N - 1
#
#         while y >= 1:
#             if board[y][x] == -2:
#                 dy = y - 1
#
#                 while dy >= 0:
#
#                     if board[y][x] != -2:
#                         break
#
#                     if board[dy][x] == -1:
#                         if dy - 1 >= 0:
#                             y = dy - 1
#                             dy = y - 1
#                         else:
#                             break
#
#                     elif board[dy][x] != -2:
#                         board[y][x], board[dy][x] = board[dy][x], -2
#                         break
#
#                     else:
#                         dy -= 1
#             y -= 1
#     return board
#
#
# def gravity(board):
#     # 열 탐색
#     for c in range(N):
#         r = N-1
#
#         # 가장 아래 행부터 올라가기
#         while r > 0:
#
#             # board[r][c] 값이 빈 값일 경우 중력 작용
#             if board[r][c] == -2:
#
#                 # 이동할 행 dr 기존 r 보타 한칸 위에서 부터 탐색
#                 dr = r - 1
#
#                 # dr 이 맨 위로 올라갈때 까지 반복 진행
#                 while dr >= 0:
#
#                     # dr 지점이 -1(벽)일 경우 dr값을 r로 바꾸고 break
#                     # 이로 인해 새로운 시작 포인트를 r로 설정 가능
#                     if board[dr][c] == -1:
#                         r = dr
#                         break
#
#                     # dr 지점이 블록일 경우 서로 값 교체
#                     # 이때 r값을 다시 dr에 지정하면 안됨
#                     elif board[dr][c] >= 0:
#                         board[r][c], board[dr][c] = board[dr][c], -2
#                         break
#
#                     # 아무것도 없을경우 dr 증가
#                     elif board[dr][c] == -2:
#                         dr -= 1
#             r -= 1
#
#     return board


def gravity(board):

    for c in range(N):
        r = N - 1

        while r >= 0:
            if board[r][c] == -2:
                dr = r - 1

                while dr >= 0:

                    if board[dr][c] == -1: # wall
                        r = dr
                        break

                    elif board[dr][c] >= 0: # block
                        board[r][c], board[dr][c] = board[dr][c], -2
                        break

                    else: # nothing
                        dr -= 1
            r -= 1

    return board


def find_group():
    total_group = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if 0 >= board[r][c]:
                continue

            base_c = board[r][c]
            visited[r][c] = 1
            cnt = 1
            reset_lst = []
            tmp_block = [[r, c]]
            que = deque([[r, c]])

            while que:
                qr, qc = que.popleft()
                for dr, dc in directions:
                    nqr = qr + dr
                    nqc = qc + dc

                    if N > nqr >= 0 and N > nqc >= 0 and visited[nqr][nqc] == 0:
                        if board[nqr][nqc] == base_c or board[nqr][nqc] == 0:

                            if board[nqr][nqc] == 0:
                                reset_lst.append([nqr, nqc])
                            else:
                                tmp_block.append([nqr, nqc])

                            cnt += 1
                            visited[nqr][nqc] = 1
                            que.append([nqr, nqc])

            if 2 > cnt:
                continue

            tmp_block.sort(key=lambda x: (x[0], x[1]))
            base_r, base_c = tmp_block[0]
            total_group.append([cnt, len(reset_lst), base_r, base_c, tmp_block, reset_lst])

            for rr, rc in reset_lst:
                visited[rr][rc] = 0

    if not total_group:
        return 0
    total_group.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))
    # print('#1', total_group)
    # print('#2', total_group[0])
    cnt, _, _, _, rest_block_color, rest_block_rain = total_group[0]

    for rr, rc in rest_block_color:
        board[rr][rc] = -2

    for rr, rc in rest_block_rain:
        board[rr][rc] = -2

    return cnt**2

answer = 0


while True:
    # print_board(board)
    # print(answer)
    rm_cnt = find_group()
    if rm_cnt == 0:
        break
    answer += rm_cnt
    # print('find group')
    # print_board(board)
    # print(rm_cnt)

    board = gravity(board)
    # print('gravity')
    # print_board(board)

    board = rot270(board)
    # print('rot')
    # print_board(board)

    # print('gravity')
    board = gravity(board)
    # print_board(board)


print(answer)
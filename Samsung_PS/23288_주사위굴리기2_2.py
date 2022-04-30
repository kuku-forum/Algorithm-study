from collections import deque

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dice = [
    [0, 2, 0],
    [4, 1, 3],
    [0, 5, 0],
    [0, 6, 0],
]

#동 남 서 북
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_board(arr):
    for row in arr:
        print(row)
    print()


def dice_move(flag):

    if flag == 0: # 동
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = \
            dice[3][1], dice[1][0], dice[1][1], dice[1][2]

    elif flag == 1: # 남
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = \
            dice[3][1], dice[0][1], dice[1][1], dice[2][1]

    elif flag == 2: # 서
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = \
            dice[1][1], dice[1][2], dice[3][1], dice[1][0]

    elif flag == 3: # 북
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = \
            dice[1][1], dice[2][1], dice[3][1], dice[0][1]



def get_socre(sr, sc):

    score = B = board[sr][sc]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[sr][sc] = 1
    que = deque([[sr, sc]])

    while que:
        r, c = que.popleft()
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if N > nr >= 0 and M > nc >= 0 and visited[nr][nc] == 0 and board[nr][nc] == B:
                que.append([nr, nc])
                visited[nr][nc] = 1
                score += board[nr][nc]
    return score


def compare_dice(nd, A, B):
    if A > B:
        return (nd + 1)%4
    elif A < B:
        return (nd - 1) % 4
    else:
        return nd

answer = 0
r, c = 0, 0
d = 0
for _ in range(K):
    dr, dc = directions[d]

    if N > r + dr >= 0 and M > c + dc >= 0:
        r += dr
        c += dc
    else:
        d = (d+2)%4
        dr, dc = directions[d]
        r += dr
        c += dc


    dice_move(d)
    answer += get_socre(r, c)
    d = compare_dice(d, dice[3][1], board[r][c])

print(answer)
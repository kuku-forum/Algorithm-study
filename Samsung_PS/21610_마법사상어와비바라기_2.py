def print_board(arr):
    for row in arr:
        print(row)
    print()


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
com_lst = [list(map(int, input().split())) for _ in range(M)]
cloud_lst = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
c_directions = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
                5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
dig_lst = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
visited = [[0 for _ in range(N)] for _ in range(N)]


def move_cloud(d, s):
    dr, dc = c_directions[d]
    dr *= s
    dc *= s

    for idx in range(len(cloud_lst)):
        cloud = cloud_lst[idx]
        new_r = (cloud[0] + dr) % N
        new_c = (cloud[1] + dc) % N
        cloud_lst[idx][0] = new_r
        cloud_lst[idx][1] = new_c
        visited[new_r][new_c] = 1
        board[new_r][new_c] += 1


def water_copy():
    for r, c in cloud_lst:
        for dr, dc in dig_lst:
            nr = r + dr
            nc = c + dc

            if N > nr >= 0 and N > nc >= 0 and board[nr][nc] > 0:
                board[r][c] += 1


def make_cloud():
    new_cloud_lst = []

    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and visited[r][c] == 0:
                board[r][c] -= 2
                new_cloud_lst.append([r, c])

    for cr, cc in cloud_lst:
        visited[cr][cc] = 0

    return new_cloud_lst

def sum_water(arr):
    result = 0
    for row in arr:
        result += sum(row)
    return result

for com in com_lst:
    move_cloud(com[0], com[1])
    water_copy()
    cloud_lst = make_cloud()

print(sum_water(board))
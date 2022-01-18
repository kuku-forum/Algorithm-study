from collections import deque

N, M = map(int, input().split())
board_lst = []
store_lst = []
home_lst = []

for i in range(N):
    row = []
    for j, k in enumerate(map(int, input().split())):
        if k == 1:
            home_lst.append([i, j])
        elif k == 2:
            store_lst.append([i, j])
            continue
        row.append(k)
    board_lst.append(row)


def print_board(arr):

    for row in arr:
        for c in row:
            if c >= 0xfff:
                print('F', end=' ')
            else:
                print(c, end=' ')
        print()
    print()


def gen_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i+1:], n-1):
            result.append([elem] + C)
    return result

def dfs(board, root):
    INF = 0xffff
    direction_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[INF for _ in range(N)] for _ in range(N)]

    # print('root', root)
    for y, x in root:
        visited[y][x] = 0

    que = deque()
    que.extend(root)

    while que:
        y, x = que.popleft()
        for direct in direction_lst:
            ny, nx = y + direct[0], x + direct[1]

            if N > ny >= 0 and N > nx >= 0:
                if visited[ny][nx] > visited[y][x] + 1:
                    visited[ny][nx] = visited[y][x] + 1
                    que.append([ny, nx])

    # print_board(visited)

    dist = 0
    for y, x in home_lst:
        dist += visited[y][x]

    return dist


store_combi = gen_combi(store_lst, M)
# print('#0', store_combi)

answer = 0xffff
for store in store_combi:
    sum_dist = dfs(board_lst, store)
    answer = min(answer, sum_dist)

print(answer)

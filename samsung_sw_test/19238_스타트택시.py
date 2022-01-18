from collections import deque, defaultdict

N, M, fuel = map(int, input().split())

board_lst = []

for _ in range(N):
    board_lst.append(list(map(int, input().split())))

ry, rx = map(int, input().split())
root = [ry-1, rx-1]

work_lst = defaultdict(list)

for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    work_lst[sy-1, sx-1] = [ey-1, ex-1]

direction_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]
# print(work_lst)

def find_guest(board, root, work):
    deq = deque([root])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[root[0]][root[1]] = 0

    while deq:
        y, x = deq.popleft()
        for direct in direction_lst:
            ny = y + direct[0]
            nx = x + direct[1]

            if N > ny >= 0 and N > nx >= 0 and board[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                deq.append([ny, nx])

    # print()
    # for row in visited:
    #     print(row)

    select_pos = []
    for pos in work:
        sy, sx = pos

        select_pos.append([visited[sy][sx], sy, sx])

    select_pos.sort(key=lambda x: (x[0], x[1], x[2]))

    return select_pos[0][0], [select_pos[0][1], select_pos[0][2]]


def find_target(board, root, target):
    deq = deque([root])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[root[0]][root[1]] = 0

    while deq:
        y, x = deq.popleft()

        if [y, x] == target:
            return [y, x], visited[y][x]

        for direct in direction_lst:
            ny = y + direct[0]
            nx = x + direct[1]

            if N > ny >= 0 and N > nx >= 0 and board[ny][nx] == 0 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                deq.append([ny, nx])
    return [-1, -1], -1


end_trigger = False
for _ in range(M):
    dist, start = find_guest(board_lst, root, work_lst)
    target = work_lst[start[0], start[1]]
    fuel -= dist
    del(work_lst[start[0], start[1]])

    # print('#1', dist, fuel, start, target, work_lst)

    root, cost = find_target(board_lst, start, target)

    if 0 > fuel - cost or dist == -1:
        print(-1)
        end_trigger = True
        break
    else:
        fuel = fuel - cost + 2*cost

if not end_trigger:
    print(fuel)
'''
1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향
2. 자신의 냄새가 있는 칸의 방향
3. 둘 중 여러개가 있으면 특정한 우선순위
위 아래 왼쪽 오른쪽
'''

from collections import deque

N, M, K = map(int, input().split())

order_lst = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board_lst = [[0 for _ in range(N)] for _ in range(N)]
shark_pos = [[] for _ in range(M)]

for i in range(N):
    for j, elem in enumerate(map(int, input().split())):
        board_lst[i][j] = elem
        if elem > 0:
            shark_pos[elem-1] = [i, j, elem]

shark_direct = list(map(int, input().split()))

direct_lst = [[] for _ in range(M)]

for i in range(M):
    tmp = []
    for idx in range(4):
        tmp2 = []
        for j in map(int, input().split()):
            tmp2.append(order_lst[j-1])
        tmp.append(tmp2)
    direct_lst[i] = tmp


def print_board(arr):
    for row in arr:
        print(row)
    print()


print_board(board_lst)
print(shark_pos)
print(shark_direct)
print_board(direct_lst)


def bfs(board, root):
    que = deque(root)
    visited = [[[0, 0] for _ in range(N)] for _ in range(N)]
    for i, pos in enumerate(root):
        visited[pos[0]][pos[1]][0] = i+1
        visited[pos[0]][pos[1]][1] = K

    print_board(visited)

    while que:
        y, x, num = que.popleft()
        no_zone = []
        my_zone = []
        for order in order_lst:
            ny = y + order[0]
            nx = x + order[1]

            if N > ny >= 0 and N > nx >= 0:
                if visited[ny][nx][1] == 0:
                    # print('#1', visited[ny][nx], num)
                    no_zone.append([ny, nx])
                if visited[ny][nx][0] == num:
                    my_zone.append([ny, nx])

        # print('no', no_zone, y, x)
        # print('my', my_zone)
        if len(no_zone) > 0:
            for direct in direct_lst[num-1][shark_direct[num-1]-1]:
                dy = y + direct[0]
                dx = x + direct[1]
                if [dy, dx] in no_zone:
                    print('no_zone', dy, dx)
                    visited[dy][dx] = [num, K]
                    que.append([dy, dx, num])
                    break

        elif len(my_zone) > 0:
            for direct in direct_lst[num-1][shark_direct[num-1]-1]:
                dy = y + direct[0]
                dx = x + direct[1]
                if [dy, dx] in my_zone:
                    print('my_zone', dy, dx)
                    visited[dy][dx] = [num, K]
                    que.append([dy, dx, num])
                    break
        else:
            continue






    return


bfs(board_lst, shark_pos)
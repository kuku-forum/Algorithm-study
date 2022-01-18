from collections import deque

N, M = map(int, input().split())

board_lst = [[0 for _ in range(M)] for _ in range(N)]
zero_lst = []
one_lst = []
root = []
direct_lst = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(N):
    for j, factor in enumerate(map(int, input().split())):
        if factor == 0:
            zero_lst.append([i, j])
            continue
        if factor == 1:
            one_lst.append([i, j])
        if factor == 2:
            root.append([i, j])
        board_lst[i][j] = factor

def print_board(arr):
    for row in arr:
        print(row)
    print()


# print_board(board_lst)
# print(empty_lst)
# print(root)

def combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for C in combi(arr[i+1:], n-1):
            result += [[elem] + C]

    return result

empty_lst = combi(zero_lst, 3)
answer = 0

def bfs(board, root, empty_lst):
    global answer

    for i in range(len(empty_lst)):
        for empty in empty_lst[i]:
            board[empty[0]][empty[1]] = 1

        visited = [[0 for _ in range(M)] for _ in range(N)]

        for y, x in root:
            visited[y][x] = 2
        for y, x in one_lst:
            visited[y][x] = 3
        for empty in empty_lst[i]:
            visited[empty[0]][empty[1]] = 3

        que = deque(root)


        while que:
            y, x = que.popleft()

            for direct in direct_lst:
                ny = y + direct[0]
                nx = x + direct[1]

                if N > ny >= 0 and M > nx >= 0 and visited[ny][nx] == 0:

                    if board[ny][nx] == 0:
                        visited[ny][nx] = 1
                        que.append([ny, nx])

        # print(empty_lst[i])
        # print_board(visited)
        cnt = 0
        for row in visited:
            for elem in row:
                if elem == 0:
                    cnt += 1

        answer = max(answer, cnt)
        # print(empty_lst[i])
        # print_board(visited)

        for empty in empty_lst[i]:
            board[empty[0]][empty[1]] = 0


bfs(board_lst, root, empty_lst)
print(answer)
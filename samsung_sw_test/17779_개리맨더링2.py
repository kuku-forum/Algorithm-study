from collections import defaultdict

N = int(input())

board_lst = []
for _ in range(N):
    board_lst.append(list(map(int, input().split())))


def boundary(board):
    answer = 0xffff

    for y in range(N):
        for x in range(N):
            for d1 in range(N):
                for d2 in range(N):
                    if 0 <= x < x + d1 + d2 <= N-1 and 0 <= y - d1 < y < y + d2 <= N-1:

                        visited = [[0 for _ in range(N)] for _ in range(N)]
                        five_district = defaultdict(list)
                        num_sum = [0 for _ in range(5)]

                        for i, j in zip([i for i in range(x, x + d1 + 1)], [i for i in range(y, y - d1 - 1, -1)]):
                            visited[i][j] = 5
                            five_district[i].append(j)

                        for i, j in zip([i for i in range(x, x + d2 + 1)], [i for i in range(y, y + d2 + 1)]):
                            visited[i][j] = 5
                            five_district[i].append(j)

                        for i, j in zip([i for i in range(x + d1, x + d1 + d2 + 2)], [i for i in range(y - d1, y - d1 + d2 + 1)]):
                            visited[i][j] = 5
                            five_district[i].append(j)

                        for i, j in zip([i for i in range(x + d2, x + d1 + d2 + 1)], [i for i in range(y + d2, y + d2 - d1 - 1, -1)]):
                            visited[i][j] = 5
                            five_district[i].append(j)

                        for r, c_lst in five_district.items():
                            c_s = min(c_lst)
                            c_e = max(c_lst)

                            for c in range(c_s, c_e + 1):
                                visited[r][c] = 5

                        for r in range(N):
                            for c in range(N):
                                if 0 <= r < x + d1 and 0 <= c <= y:
                                    if visited[r][c] != 5:
                                        visited[r][c] = 1

                                elif 0 <= r <= x + d2 and y < c < N:
                                    if visited[r][c] != 5:
                                        visited[r][c] = 2

                                elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                                    if visited[r][c] != 5:
                                        visited[r][c] = 3
                                elif x + d2 < r < N and y - d1 + d2 <= c < N:
                                    if visited[r][c] != 5:
                                        visited[r][c] = 4

                        for r in range(N):
                            for c in range(N):
                                num_sum[visited[r][c]-1] += board[r][c]

                        answer = min(answer, max(num_sum) - min(num_sum))
    return answer


result = boundary(board_lst)
print(result)

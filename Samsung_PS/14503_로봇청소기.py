'''
> 0 북, 1 동, 2 남, 3 서
> 빈 칸 0, 벽 1

'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
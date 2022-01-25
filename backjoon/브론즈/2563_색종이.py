N = int(input())

paper_list = []

for _ in range(N):
    paper_list.append(list(map(int, input().split())))
    
board = [[0 for _ in range(100)] for _ in range(100)]

side = 10

for paper in paper_list:
    sy, sx = 99 - paper[1] - side, paper[0] - 1
    ey, ex = 99 - paper[1], paper[0] + side - 1
    
    for y in range(sy, ey):
        for x in range(sx, ex):
            # print(y,x)
            board[y][x] = 1

answer = 0
for row in board:
    answer += sum(row)
print(answer)
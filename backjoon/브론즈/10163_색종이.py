N = int(input())

board = [[0 for _ in range(1002)] for _ in range(1002)]

for n in range(1, N + 1):
    sx, sy, width, heigth = map(int, input().split())
    
    for y in range(sy, sy + heigth):
        for x in range(sx, sx + width):
            board[y][x] = n
    
answer = [0 for _ in range(N + 1)]


for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] != 0:
            answer[board[i][j]] += 1
                

for val in answer[1:]:
    print(val)   
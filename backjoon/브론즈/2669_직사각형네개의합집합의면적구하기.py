pos_list = []

for _ in range(4):
    pos_list.append(list(map(int, input().split())))
    
max_x = 0
max_y = 0

for pos in pos_list:
    max_x = max(max_x, pos[-2])
    max_y = max(max_y, pos[-1])
    
board = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for pos in pos_list:
    x1, y1, x2, y2 = pos
    
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1
    
answer = 0

for row in board:
    answer += sum(row)
    
print(answer)
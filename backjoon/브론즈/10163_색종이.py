def print_board(arr):
    for row in arr:
        print(row)
    print()

N = int(input())

length = 20
# board = [[0 for _ in range(1002)] for _ in range(1002)]
board = [[0 for _ in range(length)] for _ in range(length)]
for n in range(1, N + 1):
    r1, c1, width, heigth = map(int, input().split())
    r2 = r1 + heigth - 1
    c2 = c1 + width - 1
    # print('#1', r1, c1, r2, c2)
    board[r1][c1] = 1
    board[r1][c2 + 1] = -1
    board[r2 + 1][c1] = -1
    board[r2 + 1][c2 + 1] = 1
    
print_board(board)

for r in range(length):
    for c in range(1, length):
        board[r][c] += board[r][c - 1]

# print_board(board)

for c in range(length):
    for r in range(1, length):
        
        board[r][c] += board[r - 1][c]

print_board(board)
answer = [0 for _ in range(N + 1)]


for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j] > 0:
            answer[board[i][j]] += 1
                

for val in answer[1:]:
    print(val)   
    

# N = int(input())

# board = [[0 for _ in range(1002)] for _ in range(1002)]

# for n in range(1, N + 1):
#     sx, sy, width, heigth = map(int, input().split())
    
#     for y in range(sy, sy + heigth):
#         for x in range(sx, sx + width):
#             board[y][x] = n
    
# answer = [0 for _ in range(N + 1)]


# for i in range(len(board)):
#     for j in range(len(board)):
#         if board[i][j] != 0:
#             answer[board[i][j]] += 1
                

# for val in answer[1:]:
#     print(val)   
from pprint import pprint

C, R = map(int, input().split())
K = int(input())
board = [[0 for _ in range(C)] for _ in range(R)]

direct_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
y, x = R - 1, 0

direct = 0
distance = R
flag_C = False
flag_R = True
flag_F = True
flag_out = False

while K > 1:
    
    for i in range(distance - 1):
        board[y][x] = K
        dy, dx = direct_list[direct % 4]
        y += dy
        x += dx
        K -= 1
    if 0 > K:
        print(K)
    direct += 1
    
    if flag_C:
        flag_C = False
        flag_R = True
        distance = R
        C -= 1
    else:
        flag_C = True
        flag_R = False
        distance = C
        if flag_F:
            flag_F = False
        else:
            R -= 1
    if distance == 1:
        flag_out = True
        break
    
board[y][x] = K

# pprint(board)

if flag_out:
    print(0)
else:
    print(y, x)
    
def print_board(arr):
    for row in arr:
        print(row)
    print()
    
# print_board(board)
'''
(6, 3)
(3, 5)
'''
    
    
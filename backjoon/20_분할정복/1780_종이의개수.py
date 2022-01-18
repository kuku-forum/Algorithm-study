import sys

N = int(sys.stdin.readline())

board = []

for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

cnt_m1, cnt_0, cnt_1 = 0, 0, 0

def div_board(y, x, w):
    global cnt_m1, cnt_0, cnt_1
    break_trigger = False
    init_val = board[y][x]

    for i in range(y, y+w):
        if break_trigger: break
        for j in range(x, x+w):
            if init_val == board[i][j]:
                if i == y+w-1 and j == x+w-1:
                    if init_val == -1: cnt_m1 += 1
                    elif init_val == 0: cnt_0 += 1
                    elif init_val == 1: cnt_1 += 1
            
            else:
                w //= 3
                div_board(y, x, w)
                div_board(y, x+w, w)
                div_board(y, x+2*w, w)

                div_board(y+w, x, w)
                div_board(y+w, x+w, w)
                div_board(y+w, x+2*w, w)

                div_board(y+2*w, x, w)
                div_board(y+2*w, x+w, w)
                div_board(y+2*w, x+2*w, w)
                break_trigger = True
                break
    return

div_board(0, 0, N)

print(cnt_m1)
print(cnt_0)
print(cnt_1)

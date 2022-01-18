import sys

N = int(sys.stdin.readline())
board = []

for _ in range(N):
    board.append(list(sys.stdin.readline().rstrip()))

comp_data = []

def QT(y, x, w):
    global board
    init_val = board[y][x]
    break_trigger = False

    for i in range(y, y+w):
        if break_trigger: break
        for j in range(x, x+w):
            if init_val == board[i][j]:
                if i == y+w-1 and j == x+w-1:
                    comp_data.append(init_val)
                else: continue
            else:
                w //= 2
                comp_data.append('(')
                QT(y, x, w)
                QT(y, x+w, w)
                QT(y+w, x, w)
                QT(y+w, x+w, w)
                comp_data.append(')')
                break_trigger = True
                break
    return

QT(0, 0, N)
print(*comp_data, sep='')



# N = int(input())
# image =[list(map(int, input())) for _ in range(N)]

# def solve(image):
#     state = data_check(image)
#     if state == "0":
#         return 0
#     elif state == "1":
#         return 1
#     else:
#         i_stride = int(len(image)/2)
#         code = list()
#         for i in range(2):
#             for j in range(2):
#                 patch = []
#                 for x in range(i_stride * i, i_stride * (i + 1)):
#                     tmp_list = list()
#                     for y in range(i_stride*j,i_stride*(j+1)):
#                         tmp_list.append(image[x][y])
#                     patch.append(tmp_list)

#                 tmp_code = solve(patch)
#                 code.append(tmp_code)
#         return tuple(code)

# def data_check(patch):
#     sum_ = 0
#     for i in range(len(patch)):
#         for j in range(len(patch)):
#             sum_ += patch[i][j]
#     if sum_ == 0:
#         return "0"
#     elif sum_ == len(patch)*len(patch):
#         return "1"
#     else:
#         return "Do"

# com_data = str(solve(image))
# result = com_data.replace(', ', '')
# print(result)
def print_board(arr):
    for row in arr:
        print(row)
    print()


from copy import deepcopy


# 상 좌 하 우 중력
direction_lst = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def move(board, idx):
    dr, dc = direction_lst[idx]
    
    if 1 >= idx >= 0:
        range_list = range(N)
    else:
        range_list = range(N - 1, -1, -1)
        
    for r in range_list:
        for c in range_list:
            
            if board[r][c][0] > 0:
                # print('init', r, c)
                nr = r + dr
                nc = c + dc
                # print('init', nr, nc)
                
                while True:
                    # print(nr, nc)
                    # print_board(board)
                    if nr >= N or 0 > nr or nc >= N or 0 > nc:
                        nr -= dr
                        nc -= dc
                        if (nr, nc) != (r, c):
                            board[nr][nc], board[r][c] = board[r][c], [0, 0]
                        break
                    
                    if board[nr][nc][0] > 0:
                        # print('#2', nr, nc, board[nr][nc])
                        if board[nr][nc][1] == 1 or board[nr][nc][0] != board[r][c][0] or board[r][c][1] == 1:
                            nr -= dr
                            nc -= dc
                            # print('#3', nr, nc, r, c)
                            if (nr, nc) != (r, c):
                                board[nr][nc], board[r][c] = board[r][c], [0, 0]
                        
                        elif board[nr][nc][0] == board[r][c][0]:
                            board[nr][nc][0] += board[r][c][0]
                            board[nr][nc][1] = 1
                            board[r][c] = [0, 0]
                        break                        
                    
                    nr += dr
                    nc += dc
    
    return board
                    

def max_board(board):
    result = -1
    for r in range(N):
        for c in range(N):
            result = max(result, board[r][c][0])
    return result

answer = -1


def dfs(cnt, board, test):
    global answer
    if cnt >= 1 and answer >= max_board(board) * (2**(5-cnt)):
        return
    
    if cnt == 5:
        answer = max(answer, max_board(board))
        # if tmp_answer == 32:
        #     print(test)
        #     print_board(board)
        return
        
    for selector in range(4):
        test.append(selector)
        n_board = move(deepcopy(board), selector)
        
        for r in range(N):
            for c in range(N):
                n_board[r][c][1] = 0
        dfs(cnt + 1, deepcopy(n_board), test)
        test.pop()
    
    return


N = int(input())

arr = []
for _ in range(N):
    row = []
    for e in map(int, input().split()):
        row.append([e, 0])
    arr.append(row)
test = []
dfs(0, deepcopy(arr), test)
print(answer)











# 상 좌 하 우 중력
# 상, 상, 우,하,좌
# [0, 0, 3, 2, 1]
# print_board(arr)
# print('-----------------------------')

# arr = move(arr, 0)
# print('상')
# print_board(arr)

# print('-----------------------------')
# arr = move(arr, 0)
# print('상')
# print_board(arr)

# print('-----------------------------')
# arr = move(arr, 3)
# print('우')
# print_board(arr)

# print('-----------------------------')
# arr = move(arr, 2)
# print('하')
# print_board(arr)

# print('-----------------------------')
# arr = move(arr, 1)
# print('좌')
# print_board(arr)

'''

3
2 2 2
4 4 4
8 8 8

4
0 0 2 0
0 0 0 0
2 0 0 0
0 0 0 0

4
0 0 0 0
0 0 0 0
2 0 0 0
0 0 0 0

4
4 2 0 0
0 0 0 0
0 0 0 0
2 0 0 0

4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

4
2 0 2 8
0 0 2 2
0 0 0 0
0 0 0 0


4
2 4 16 8
8 4 0 0
16 8 2 0
2 8 2 0

4
2 4 8 2
2 4 0 0
2 0 0 0
2 0 2 0

4
2 0 0 0
2 2 0 0
2 0 0 0
0 0 0 0

'''

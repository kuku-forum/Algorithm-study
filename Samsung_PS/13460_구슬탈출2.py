from collections import deque
from copy import deepcopy

def print_board(arr):
    for row in arr:
        print(row)
    print()


def rot90(arr):
    return list(map(deque, zip(*reversed(arr))))


def L_gravity(board):
    red_flag = False
    blue_flag = False
    
    for i in range(1, len(board)-1):
        row = deque([])
        
        while board[i]:
            if not row:
                row.append(board[i].popleft())
            
            if board[i][0] == 'R':
                point = 0
                while True:
                    if row[-1] == '#' or row[-1] == 'B':
                        row.append(board[i].popleft())
                        break
                    elif row[-1] == 'O':
                        point += 1
                        board[i].popleft()
                        red_flag = True
                        break
                    else:
                        row.pop()
                        point += 1
                        
                for _ in range(point):
                    row.append('.')
                    
                    
            elif board[i][0] == 'B':
                point = 0
                while True:
                    if row[-1] == '#' or row[-1] == 'R':
                        row.append(board[i].popleft())
                        break
                    elif row[-1] == 'O':
                        point += 1
                        board[i].popleft()
                        blue_flag = True
                        return board, 2
                        break
                    else:
                        row.pop()
                        point += 1
                        
                for _ in range(point):
                    row.append('.')
                    
            else:
                row.append(board[i].popleft())
                
        board[i] = row
        
    if red_flag and not blue_flag:
        return board, 1
    
    elif blue_flag and not red_flag:
        return board, 2
    else:
        return board, 3

def R_gravity(board):
    red_flag = False
    blue_flag = False
    
    for i in range(1, len(board)-1):
        row = deque([])
        
        while board[i]:
            if not row:
                row.appendleft(board[i].pop())
            
            if board[i][-1] == 'R':
                point = 0
                while True:
                    if row[0] == '#' or row[0] == 'B':
                        row.appendleft(board[i].pop())
                        break
                    elif row[0] == 'O':
                        point += 1
                        board[i].pop()
                        red_flag = True
                        break
                    else:
                        row.popleft()
                        point += 1
                        
                for _ in range(point):
                    row.appendleft('.')
                    
                    
            elif board[i][-1] == 'B':
                point = 0
                while True:
                    if row[0] == '#' or row[0] == 'R':
                        row.appendleft(board[i].pop())
                        break
                    elif row[0] == 'O':
                        point += 1
                        board[i].pop()
                        blue_flag = True
                        return board, 2
                        break
                    else:
                        row.popleft()
                        point += 1
                        
                for _ in range(point):
                    row.appendleft('.')
                    
            else:
                row.appendleft(board[i].pop())
                
        board[i] = row
    
    
    if red_flag and not blue_flag:
        return board, 1
    
    elif blue_flag and not red_flag:
        return board, 2
    
    else:
        return board, 3



def dfs(board, flag, cnt, test):
    global answer
    
    if cnt == 11:
        return 
    
    if cnt >= answer:
        return
    
    if flag == 2:
        return
    
    if flag == 1 and answer > cnt:
        answer = cnt
        return 
    
    n_board, flag = L_gravity(deepcopy(board))
    if n_board != board:
        dfs(n_board, flag , cnt + 1, deepcopy(test + [1]))
    
    n_board, flag = R_gravity(deepcopy(board))
    if n_board != board:
        dfs(n_board, flag , cnt + 1, deepcopy(test + [2]))
    
    board = rot90(board)
    
    n_board, flag = L_gravity(deepcopy(board))
    if n_board != board:
        dfs(n_board, flag , cnt + 1, deepcopy(test + [3]))
    
    n_board, flag = R_gravity(deepcopy(board))
    if n_board != board:
        dfs(n_board, flag , cnt + 1, deepcopy(test + [4]))
    
    

N, M = map(int, input().split())
board = [deque(input()) for _ in range(N)]
answer = 0xffff

dfs(board, False, 0, [])

if answer == 0xffff:
    print(-1)
else:
    print(answer)


# n_board, flag = L_gravity(deepcopy(board))
# print_board(n_board)

# n_board, flag = R_gravity(deepcopy(board))
# print_board(n_board)

# board = rot90(board)
# print_board(board)

# n_board, flag = L_gravity(deepcopy(board))
# print_board(n_board)

# n_board, flag = R_gravity(deepcopy(board))
# print_board(n_board)



# n_board, flag = R_gravity(deepcopy(board))
# print_board(n_board)

# n_board = rot90(n_board)
# # print_board(board)

# n_board, flag = L_gravity(deepcopy(n_board))
# print_board(n_board)

# n_board = rot90(n_board)
# # print_board(board)

# n_board, flag = L_gravity(deepcopy(n_board))
# print_board(n_board)
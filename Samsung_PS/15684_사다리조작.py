from pprint import pprint
from itertools import combinations

N, M, H = map(int, input().split())

board = [[0 for _ in range(N + 2)] for _ in range(H + 1)]


for _ in range(M):
    y, x = map(int, input().split())
    board[y][x] = x
    board[y][x + 1] = x

candi_list = []

for i in range(1, H + 1):
    for j in range(1, N + 1):
        if board[i][j] == 0 and board[i][j + 1] == 0:
            candi_list.append((i, j))
            

def play():
    
    for start_col in range(N, 0, -1):
        col = start_col
        
        for row in range(1, H + 1):
            if board[row][col] != 0:
                if board[row][col] == board[row][col - 1]:
                    col -= 1
                elif board[row][col] == board[row][col + 1]:
                    col += 1
        else:
            if col != start_col:
                return False
    return True
    
    
def combi_gen(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for C in combi_gen(arr[i + 1:], n - 1):
            result.append([elem] + C)
    
    return result


def solution():
    
    for i in range(0, 4):
        # candi_combi = combi_gen(candi_list, i)
        candi_combi = combinations(candi_list, i)
        print(list(candi_combi))
        print()
        
        for candi in candi_combi:
            for ny, nx in candi:
                board[ny][nx] = nx
                board[ny][nx + 1] = nx
            
            if play():
                pprint(board)
                return i
            
            for ny, nx in candi:
                board[ny][nx] = 0
                board[ny][nx + 1] = 0
                
    return -1
pprint(board)
print()
answer = solution()
print(answer)

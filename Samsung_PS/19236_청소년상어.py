'''
> 물고기를 dict에 넣고, 삭제시 del

> 물고기 이동 함수
> ↑, ↖, ←, ↙, ↓, ↘, →, ↗
> 시계방향으로 list 만들고 하나씩 증가 시키면서 전방 탐색
> 이동 가능할 경우 서로 위치 바꾸기


> 상어 이동
 DFS로 구성
 1. 방향에 따라 접근 가능한 board위치 list로 추출
 2. list가 없을경우 return
 3. 있을경우 해당 물고기를 먹고 재귀 dfs, deepcopy로 진행
'''

def print_board(arr):
    for row in arr:
        print(row)
    print()


from copy import deepcopy
from re import L


board = []
fish_dic = {}

for i in range(4):
    arr = list(map(int, input().split()))
    row = []
    for j in range(0, 7, 2):
        row.append([arr[j], arr[j + 1] - 1])
        fish_dic[arr[j]] = (i, j//2, arr[j + 1] - 1)
    board.append(row)
    



direction_list = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def fish_wave():
    for fish in range(1, 17):
        
        if fish not in fish_dic:
            continue
        r, c, d = fish_dic[fish]
        print(fish, r, c, d)
        
        for i in range(8):
            nd = (d + i)%8
            dr, dc = direction_list[nd]
            nr, nc = r + dr, c + dc
            
            if 4 > nr >= 0 and 4 > nc >= 0 and board[nr][nc][0] > 0:
                
                board[nr][nc], board[r][c] = board[r][c], board[nr][nc]
                fish_dic[fish] = (nr, nc, nd)    
                break
        
        print_board(board)
            
            
def shark_wave():
    return

del fish_dic[board[0][0][0]]
answer, board[0][0][0] = board[0][0][0], 0

print(fish_dic)
print_board(board)

fish_wave()
print_board(board)
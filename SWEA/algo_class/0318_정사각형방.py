from my_package.hjtc import swea_tc as print
def print_board(arr):
    for row in arr:
        print(row)
    print()


from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(root):
    que = deque([root])
    cnt = 1
    cur_num = board[root[0]][root[1]]
    
    while que:
        r, c = que.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            
            if N > nr >= 0 and N > nc >= 0 and board[nr][nc] == cur_num + 1:
                que.append([nr, nc])
                cur_num = board[nr][nc]
                board[nr][nc] = 0
                cnt += 1
                break
    return cnt

for t in range(1, int(input()) + 1):
    answer = []
    max_val = 0
    N = int(input())
    board = []
    idx_list = [0 for _ in range(N**2 + 1)]
    
    for i in range(N):
        row = []
        for j, k in enumerate(map(int, input().split())):
            row.append(k)
            idx_list[k] = [i, j]
        board.append(row)
    
    for i, j in idx_list[1:]:
        num = board[i][j]
        if num == 0:
            continue
        
        tmp_val = bfs([i, j])
        
        if tmp_val > max_val:
            answer = [num, tmp_val]
            max_val = tmp_val
            
        elif tmp_val == max_val:
            if answer[0] > num:
                answer = [num, tmp_val]

    print(f'#{t} {" ".join(map(str, answer))}')
    
from my_package.hjtc import swea_tc

    
directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def dfs(n, r):
    global answer
    
    if n == N:
        answer += 1
        return
            
    for c in range(N):
        if c_lst[c] == 1:
            continue
        
        if board[r][c] == 0:
            flag = False
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                while N > nr >= 0 and N > nc >= 0:
                    if board[nr][nc] == 1:
                        flag = True
                        break
                    nr += dr
                    nc += dc
                if flag:
                    break
            else:
                board[r][c] = 1
                c_lst[c] = 1
                dfs(n+1, r+1)
                board[r][c] = 0
                c_lst[c] = 0

for t in range(1, int(input())+1):
    answer = 0
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    c_lst = [0 for _ in range(N)]
    dfs(0, 0)
    print(f'#{t} {answer}')

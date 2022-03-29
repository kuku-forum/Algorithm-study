from my_package.hjtc import swea_tc


def dfs(r, c, ssum):
    global answer
    
    if r == N-1 and c == N-1:
        answer = min(answer, ssum+board[r][c])
        return
    
    if ssum >= answer:
        return
    
    if r == N-1:
        dfs(r, c+1, ssum + board[r][c])
    elif c == N-1:
        dfs(r+1, c, ssum + board[r][c])
    else:
        dfs(r, c+1, ssum + board[r][c])
        dfs(r+1, c, ssum + board[r][c])

for t in range(1, int(input()) + 1):
    
    answer = 0xffff
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    dfs(0, 0, 0)
    
    print(f'#{t} {answer}')

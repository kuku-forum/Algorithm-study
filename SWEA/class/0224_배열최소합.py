def dfs(row, col, sum_val):
    global answer
    if sum_val >= answer:
        return
    
    if row == N:
        answer = min(answer, sum_val)
        return
    
    for c in range(N):
        if col[c] == 0:
            col[c] = 1
            dfs(row + 1, col[::], sum_val + board[row][c])
            col[c] = 0
    
    
    return

for t in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 1000000
    dfs(0, [0 for _ in range(N)], 0)
    
    print(f'#{t} {answer}')
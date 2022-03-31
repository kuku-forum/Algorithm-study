# from my_package.hjtc import swea_tc # as print

def dfs(r, total_percent):
    global max_percent
    # # 1번 가지치기: 재귀를 통해 total_percent가 0 일경우
    # if total_percent == 0:
    #     return
    
    if max_percent > total_percent:
        return
    
    if r == N:
        max_percent = total_percent
        return
    
    for c in range(N):
        # 2번 가지치기: for를 통해 board[r][c]가 0 일경우
        if board[r][c] == 0:
            continue
        
        if c_visited[c] == 0:
            c_visited[c] = 1
            dfs(r+1, total_percent*board[r][c])
            c_visited[c] = 0
            
            
def convert(x):
    return int(x)*0.01


for t in range(1, int(input())+1):
    max_percent = 0
    N = int(input())
    board = [list(map(convert, input().split())) for _ in range(N)]
    c_visited = [0 for _ in range(N)]
    
    dfs(0, 1)
    print(f'#{t} {max_percent*100:0.6f}')
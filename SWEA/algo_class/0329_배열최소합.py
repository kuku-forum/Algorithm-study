from my_package.hjtc import swea_tc

def DFS(r, used, ssum):
    global answer
    
    if r == N:
        answer = min(answer, ssum)
        return
    
    if ssum >= answer:
        return
    
    for c in range(N):
        if c not in used:
            DFS(r+1, used + [c], ssum + board[r][c])
    

for t in range(1, int(input()) + 1):
    
    answer = 0xffff
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    DFS(0, [], 0)
    print(f'#{t} {answer}')

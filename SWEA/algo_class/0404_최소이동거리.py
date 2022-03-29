from my_package.hjtc import swea_tc

def print_board(arr):
    for row in arr:
        print(row)
    print()

def dfs(start, ssum):
    global answer
    if ssum >= answer:
        return
    
    if start == N:
        answer = min(answer, ssum)
        return
    
    for end in range(N+1):
        if start == end or dist[start][end] == INF:
            continue
        
        dfs(end, ssum + dist[start][end])
    

for t in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    INF = 100000000
    answer = INF
    case_lst = [[] for _ in range(N+1)]
    dist = [[INF for _ in range(N+1)] for _ in range(N+1)]
    
    
    for _ in range(E):
        s, e, w = map(int, input().split())
        dist[s][e] = min(dist[s][e], w)
    
    dfs(0, 0)
    
    print(f'#{t} {answer}')
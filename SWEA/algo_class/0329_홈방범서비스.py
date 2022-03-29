from my_package.hjtc import swea_tc



def dfs(service_lst):
    global answer
    
    for r in range(N):
        for c in range(N):
            cnt = 0
            
            for dr, dc in service_lst:
                nr = r + dr
                nc = c + dc
                
                if N > nr >= 0 and N > nc >= 0:
                    if board[nr][nc] == 1:
                        cnt += 1
                        
            if cnt*M - len(service_lst) >= 0:
                answer = max(answer, cnt)
    return

for t in range(1, int(input()) + 1):
    
    answer = 0
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    service_lst = [(0, 0)]
    
    for K in range(M+3):
        
        for i in range(len(service_lst)):
            nr, nc = service_lst[i]
            
            for dr, dc in directions:
                service_lst.append((nr + dr, nc + dc))
        
        # print(K, len(set(service_lst)), set(service_lst))
        dfs(set(service_lst))
    
    print(f'#{t} {answer}')
    # break
from my_package.hjtc import swea_tc

def dfs(r, total_cost):
    global answer
    
    # 최솟값(answer) 보다 클 경우 가지치기
    if total_cost >= answer:
        return
    
    # r(행)이 N에 다다르면 최솟값 갱신    
    if r == N:
        answer = total_cost
        return
    
    # c(열) 순회
    for c in range(N):
        
        # c 사용여부 확인, 사용하지 않았다면 사용표시 후 초기화
        if c_visited[c] == 0:
            c_visited[c] = 1
            # r 및 total_cost를 증가시키며 dfs 진행
            dfs(r+1, total_cost+board[r][c])
            c_visited[c] = 0
            
            
for t in range(1, int(input())+1):
    # 초기값 세팅
    answer = 15*15*99
    N = int(input())
    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    c_visited = [0 for _ in range(N)]
    dfs(0, 0)
        
    print(f'#{t} {answer}')
from my_package.hjtc import swea_tc as print

T = int(input())

for t in range(1, T + 1):
    
    N, Q = map(int, input().split())
    board = [0 for _ in range(N)]
    
    for i in range(Q):
        i += 1
        L, R = map(int, input().split())
        
        for j in range(L - 1, R):
            board[j] = i
        
    answer = ' '.join(map(str, board))  
    print(f'#{t} {answer}')
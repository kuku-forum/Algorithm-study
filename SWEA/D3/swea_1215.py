from my_package.hjtc import swea_tc

for t in range(1, 11):
    answer = 0
    
    N = int(input())
    board = []
    for _ in range(8):
        board.append(input())
    
    for i in range(8):
        for j in range(8 - N + 1):
            for n in range(N//2):
                if j + n > N + j - n - 1:
                    break
                if board[i][j + n] != board[i][N + j - n - 1]:
                    break
            else:
                answer += 1
            
                
    for i in range(8 - N + 1):
        for j in range(8):
            
            for n in range(N//2):
                if i + n > N + i - n - 1:
                    break
                if board[i + n][j] != board[N + i - n - 1][j]:
                    break
            else:
                answer += 1
    
    swea_tc(f'#{t} {answer}')
    
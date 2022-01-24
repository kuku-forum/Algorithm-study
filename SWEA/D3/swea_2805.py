T = int(input())

for t in range(1, T + 1):
    
    N = int(input())
    board = []
    
    for _ in range(N):
        board.append(list(map(int, input())))
    
    if N == 1:
        answer = board[0][0]
        print(f'#{t} {answer}')
    else:
        mid_pos = N//2
        answer = sum(board[mid_pos])
        
        for x, y in enumerate(range(mid_pos + 1, N)):
            answer += sum(board[y][x + 1:N - x - 1])
            answer += sum(board[N - y - 1][x + 1:N - x - 1])
        print(f'#{t} {answer}')
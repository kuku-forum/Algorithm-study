T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = []
    
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    direct_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    answer = 0
    
    for i in range(N):
        for j in range(N):
            for di, dj in direct_list:
                if N > i + di >= 0 and N > j + dj >= 0:
                    answer += abs(board[i + di][j + dj] - board[i][j])
                    
    
    print(f'#{t} {answer}')
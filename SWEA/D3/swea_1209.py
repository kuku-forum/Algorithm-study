from my_package.hjtc import swea_tc


for t in range(1, 11):
    _ = input()
    answer = []
    board = []
    
    for _ in range(100):
        row = list(map(int, input().split()))
        board.append(row)
        answer.append(sum(row))
        
    for x in range(100):
        col_sum = 0
        for y in range(100):
            col_sum += board[y][x]
        answer.append(col_sum)
        
    dig_m_sum = 0
    dig_p_sum = 0
    
    for i in range(100):
        dig_m_sum += board[i][i]
        dig_p_sum += board[i][99-i]
        
    answer.extend([dig_m_sum, dig_p_sum])
        
    print(f'#{t} {max(answer)}')
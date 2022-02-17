from my_package.hjtc import swea_tc as print

for t in range(1, 11):
    answer = 0
    
    _ = int(input())
    board = []
    N = 100
    for _ in range(100):
        board.append(input())
        

    for y in range(N):
        flag = False
        
        for window in range(N - 1, -1, -1): # 99, 98, 97, 0
            for idx in range(N - window): # 1, 2, 3, 4, 100
                start = idx
                end = start + window
                while end >= start:
                    if board[y][start] != board[y][end]:
                        break
                    
                    start += 1
                    end -= 1
                else:
                    answer = window + 1 if window + 1 > answer else answer
                    flag = True
                    break
            if flag:
                break
            
    for x in range(N):
        flag = False
        
        for window in range(N - 1, -1, -1): # 99, 98, 97, 0
            for idx in range(N - window): # 1, 2, 3, 4, 100
                start = idx
                end = start + window
                while end >= start:
                    if board[start][x] != board[end][x]:
                        break
                    
                    start += 1
                    end -= 1
                else:
                    answer = window + 1 if window + 1 > answer else answer
                    flag = True
                    break
            if flag:
                break
                
                
    print(f'#{t} {answer}')
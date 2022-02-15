T = int(input())

def solution(board):
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            chk_lst = [-1 for _ in range(10)]
            
            for dy in range(3):
                for dx in range(3):
                    ny = y + dy
                    nx = x + dx
                    num = board[ny][nx]
                    
                    if chk_lst[num] == -1:
                        chk_lst[num] = 0
                    else:
                        return 0
    
    for y in range(9):
        x_chk_lst = [-1 for _ in range(10)]
        
        for x in range(9):
            num = board[y][x] 
            if x_chk_lst[num] == -1:
                x_chk_lst[num] = 0
            else:
                return 0
            
            y_chk_lst = [-1 for _ in range(10)]
            for dy in range(9):
                num = board[dy][x] 
                if y_chk_lst[num] == -1:
                    y_chk_lst[num] = 0
                else:
                    return 0
                        
    return 1

for t in range(1, T + 1):
    arr = []
    for _ in range(9):
        arr.append(list(map(int, input().split())))
        
    answer = solution(arr)
    print(f'#{t} {answer}')
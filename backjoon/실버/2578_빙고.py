from pprint import pprint

board = []
pos_dic = {}

for i in range(5):
    row = []
    for j, num in enumerate(map(int, input().split())):
        row.append(num)
        pos_dic[num] = (i, j)
    board.append(row)    

cnt = 0
answer = 0

flag = False

for i in range(5):
    
    for j, num in enumerate(map(int, input().split())):
        cnt += 1
        y, x = pos_dic[num]
        board[y][x] = 0

        if i >= 2:
            bingo = 0
            
            for row in board:
                if sum(row) == 0:
                    bingo += 1
                    
            for j in range(5):
                col_sum = 0
                for i in range(5):
                    col_sum += board[i][j]
                    
                if col_sum == 0:
                    bingo += 1
                
            dig_bingo = 0 
            dig_rev_bingo = 0   
            for dig in range(5):
                dig_bingo += board[dig][dig]
                dig_rev_bingo += board[-(dig + 1)][dig]
                
            if dig_bingo == 0:
                bingo += 1
                
            if dig_rev_bingo == 0:
                bingo += 1
            
            if bingo >= 3:
                flag = True
                answer = cnt
                break
    if flag:
        break

print(answer)

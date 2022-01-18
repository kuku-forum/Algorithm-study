row, column = map(int, input().split())
maps= []
window = 8

for _ in range(row):
    maps.append(input())

answer = []

for start_cnt in range(0, row-window+1):
    for col_idx in range(0, column-window+1):
        stop_cnt = 0
        W_cnt = 0
        B_cnt = 0
        for row_idx in range(row):    
            tmp_map = maps[row_idx+start_cnt][col_idx:col_idx+window]
            
            for idx, cell in enumerate(tmp_map):
                # case1 start_cell=white
                if row_idx%2 == 0 and idx%2 == 0 and cell != 'W':
                    W_cnt += 1
                elif row_idx%2 == 0 and idx%2 == 1 and cell != 'B':
                    W_cnt += 1
                elif row_idx%2 == 1 and idx%2 == 0 and cell != 'B':
                    W_cnt += 1
                elif row_idx%2 == 1 and idx%2 == 1 and cell != 'W':
                    W_cnt += 1
                
                # case2 start_cell=black
                if row_idx%2 == 0 and idx%2 == 0 and cell != 'B':
                    B_cnt += 1
                elif row_idx%2 == 0 and idx%2 == 1 and cell != 'W':
                    B_cnt += 1
                elif row_idx%2 == 1 and idx%2 == 0 and cell != 'W':
                    B_cnt += 1
                elif row_idx%2 == 1 and idx%2 == 1 and cell != 'B':
                    B_cnt += 1
            
                    
            stop_cnt += 1
            
            if stop_cnt == window:
                answer.append(W_cnt)
                answer.append(B_cnt)
                break

print(min(answer))
def star_maker(n):
    
    if n == 3: return [[1,1,1],[1,0,1],[1,1,1]]
    
    tmp_map = [[1 for _ in range(n)] for _ in range(n)]
    window = n//3
    sub_map = star_maker(n//3)
    
    for row in range(n): # 0,1,2,3,4,5,6,7,8,9,10,11---,26
        for column in range(0, n, window): #0,3,6,9,12,15,18,21,24
        
            if window <= row < 2*window and window <= column < 2*window:
                tmp_map[row][column:column+window] = [0 for _ in range(window)]
            else:
                # print(n)
                tmp_map[row][column:column+window] = sub_map[row % window]
    
    return tmp_map
        

T = int(input())

for row in star_maker(T):
    for column in row:
        if column: print('*', end='')
        else: print(' ', end='')
    print()    
from my_package.hjtc import swea_tc

def gen_combi(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        for C in gen_combi(arr[i + 1:], n - 1):
            result.append([arr[i]] + C)
            
    return result

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    min_val = 0xffff
    
    for _ in range(N):
        row = input()
        w = M - row.count('W')
        b = M - row.count('B')
        r = M - row.count('R')
        board.append([w, b, r])
    
    boundary = gen_combi([n for n in range(1, N)], 2)
    from pprint import pprint
    
    for b1, b2 in boundary:
        tmp_val = 0
        for row in board[:b1]:
            tmp_val += row[0]
            
        for row in board[b1:b2]:
            tmp_val += row[1]
            
        for row in board[b2:]:
            tmp_val += row[2]

        min_val = min(min_val, tmp_val)
        
    swea_tc(f'#{t} {min_val}')
    
    
    
    
        
        
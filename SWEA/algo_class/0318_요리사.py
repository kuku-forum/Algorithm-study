from my_package.hjtc import swea_tc as print
from itertools import combinations

def gen_combi(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        e = arr[i]
        for C in gen_combi(arr[i+1:], n-1):
            result.append([e] + C) 
            
    return result
    
    
for t in range(1, int(input()) + 1):
    N = int(input())    
    board = [list(map(int, input().split())) for _ in range(N)]
    
    answer = 160000
    idx_lst = [i for i in range(N)]
    combi_idx = list(combinations(idx_lst, N//2))
    
    for idx in range(len(combi_idx)//2):
        synergy1 = synergy2 = 0
        
        for i, j in combinations(combi_idx[idx], 2):
            synergy1 += (board[i][j] + board[j][i])
        
        for i, j in combinations(combi_idx[-(idx+1)], 2):
            synergy2 += (board[i][j] + board[j][i])
            
        diff = abs(synergy1 - synergy2)
        answer = min(answer, diff)
        
    print(f'#{t} {answer}')
    
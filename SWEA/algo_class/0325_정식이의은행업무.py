from my_package.hjtc import swea_tc
from pprint import pprint

def print_board(arr):
    for row in arr:
        print(row)
    print()

def chk():
    for r1 in range(len(board2)):
        for c1 in range(2):
            n_sum_n2 = sum_n2 + board2[r1][c1]
            
            for r2 in range(len(board3)):
                for c2 in range(3):
                    n_sum_n3 = sum_n3 + board3[r2][c2]
                    
                    if n_sum_n2 == n_sum_n3:
                        return n_sum_n2
    return

for t in range(1, int(input()) + 1):
    
    n2 = list(map(int, input()))[::-1]
    n3 = list(map(int, input()))[::-1]
    
    sum_n2 = sum(n*pow(2, i) for i, n in enumerate(n2))
    sum_n3 = sum(n*pow(3, i) for i, n in enumerate(n3))
    answer = 0
    
    board2 = [[0 for _ in range(2)] for _ in range(len(n2))]
    board3 = [[0 for _ in range(3)] for _ in range(len(n3))]
    
    for r in range(len(n2)):
        std_n = n2[r]
        mul_n = pow(2, r)
        for c in range(2):
            if std_n == c:
                continue
            
            if c > std_n:
                board2[r][c] = c*mul_n - std_n*mul_n
            else:
                board2[r][c] = c*mul_n - std_n*mul_n
            
    for r in range(len(n3)):
        std_n = n3[r]
        mul_n = pow(3, r)
        for c in range(3):
            if std_n == c:
                continue
            
            if c > std_n:
                board3[r][c] = c*mul_n - std_n*mul_n
            else:
                board3[r][c] = c*mul_n - std_n*mul_n
                
    board2[len(n2)-1][0] = 0
    board3[len(n3)-1][0] = 0
    
    answer = chk()
    
    print(f'#{t} {answer}')
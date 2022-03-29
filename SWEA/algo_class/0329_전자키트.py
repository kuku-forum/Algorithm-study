from my_package.hjtc import swea_tc
from itertools import permutations


for t in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    rooms = [n for n in range(1, N)]
    
    path_lst = list(permutations(rooms, N-1))
    
    answer = 0xffff
    for path in path_lst:
        prev = 0
        tmp = 0
        for p in path:
            tmp += board[prev][p]
            prev = p
        tmp += board[prev][0]
        
        answer = min(answer, tmp)
        
    print(f'#{t} {answer}')
            
    
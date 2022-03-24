from my_package.hjtc import swea_tc
from pprint import pprint

# 상 좌 하 우 변경
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for t in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    answer = 0
    board = [[[] for _ in range(N)] for _ in range(N)]
    microbe_dic = {}
    keys = []
    
    for idx in range(K):
        r, c, n, d = map(int, input().split())
        d -= 1
        if d == 1:
            d = 2
        elif d == 2:
            d = 1
        board[r][c].append(idx)
        microbe_dic[idx] = [r, c, n, d]
        keys.append([r, c])
    
    for _ in range(M):
        
        overlap_set = set()
        new_key = set()
        move_lst = []
        
        for key in keys:
            
            while board[key[0]][key[1]]:
                idx = board[key[0]][key[1]].pop()
                r, c, n, d = microbe_dic[idx]
                dr, dc = directions[d]
                nr = r + dr
                nc = c + dc
                
                if nr == N-1 or nr == 0 or nc == N-1 or nc == 0:
                    d = (d + 2)%4
                    n //= 2
                
                if n == 0:
                    continue
                
                microbe_dic[idx] = [nr, nc, n, d]
                new_key.add((nr, nc))
                move_lst.append([nr, nc, idx])
        
        keys = new_key
        for r, c, idx in move_lst:
            board[r][c].append(idx)
            if len(board[r][c]) >= 2:
                overlap_set.add((r, c))
        
        for rr, rc in overlap_set:
            max_num = 0
            max_idx = ''
            total_num = 0
            
            for idx in board[rr][rc]:
                r, c, n, d = microbe_dic[idx]
                total_num += n
                if n > max_num:
                    max_idx = idx
                    max_num = n
            
            microbe_dic[max_idx][2] = total_num
            
            for idx in board[rr][rc]:
                if max_idx != idx:
                    del microbe_dic[idx]
                    
            board[rr][rc] = [max_idx]
        
    for key in microbe_dic.keys():
        answer += microbe_dic[key][2]
    
    print(f'#{t} {answer}')
    
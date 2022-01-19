T = int(input())

def solution(num):
    graph = [[0 for _ in range(num)] for _ in range(num)]
    graph[0] = [n for n in range(1, num + 1)]
    dirc_lst = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    y, x = 0, num - 1
    cnt = 0
    
    for n in range(num-1, 0, -1):
        
        for _ in range(2):
            dirc_idx = cnt%4
            dy, dx = dirc_lst[dirc_idx]
            cnt += 1
            
            for _ in range(n):
                y += dy
                x += dx
                num += 1
                graph[y][x] = num
    
    return graph

'''
    동 남 서 북 동 남 서 북 동 남 서 북
3:  2  2  2  1  1
4:  3  3  3  2  2  1  1
5:  4  4  4  3  3  2  2  1  1
6:  5  5  5  4  4  3  3  2  2  1 1
'''
for t in range(1, T + 1):
    
    board = solution(int(input()))
    print(board)
    print(f'#{t}')
    for row in board:
        print(' '.join(map(str, row)))
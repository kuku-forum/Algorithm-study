from my_package.hjtc import swea_tc


def print_board(arr):
    for row in arr:
        print(row)
    print()

for t in range(1, 11):
    # answer = 0
    # N = int(input())
    # board = []
    
    # for _ in range(N):
    #     board.append(list(map(int, input().split())))
    
    # 1은 N극
    # 2는 S극
    # for x in range(N):
    #     for y in range(N):
    #         if board[y][x] == 1:
    #             break
    #         board[y][x] = 0
    
    # for x in range(N):
    #     for y in range(N-1, -1, -1):
    #         if board[y][x] == 2:
    #             break
    #         board[y][x] = 0
            
    # for x in range(N):
    #     NS = [0, 0]
    #     for y in range(N):
                
    #         if board[y][x] == 1:
    #             if sum(NS) == 2:
    #                 answer += 1
    #                 NS = [0, 0]
                    
    #             NS[0] = 1
                
                
    #         elif board[y][x] == 2:
    #             NS[1] = 1
    n = int(input())
    mag = [list(map(int, input().split())) for _ in range(n)]  # 1: N, 2: S
 
    total_res = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if mag[j][i] == 1:
                flag = 1
            elif mag[j][i] == 2:
                if flag :
                    total_res += 1
                    flag = 0

    swea_tc(f'#{t} {total_res}')
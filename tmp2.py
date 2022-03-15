from pprint import pprint 

def solution(n, clockwise):
    answer = [[]]

    board = [[0 for _ in range(n)] for _ in range(n)]
    
    

    if clockwise:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        start_point_list = [(0, 0), (0, n-1), (n-1, n-1), (n-1, 0)]
    else:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        start_point_list = [(0, 0), (n-1, 0), (n-1, n-1), (0, n-1)]
    
    for r, c in start_point_list:
        board[r][c] = 1
    
    for i, (r, c) in enumerate(start_point_list):
        move = 0
        step = n - 2
        cnt = 2
        rot = 0
        while step >= 1:
            # print(step)
            dr, dc = directions[(i + rot)%4]
            
            for  _ in range(step):
                r += dr
                c += dc
                # pprint(board)
                # print()
                board[r][c] = cnt
                cnt += 1
            rot += 1
            move += 2
            step = n - 1 - move
            # print(step, move)
            
    if n % 2 == 1:
        board[n//2][n//2] = cnt
    print(cnt)
    pprint(board)
    print()
    return answer

solution(5, True)
solution(6, False)
solution(9, False)
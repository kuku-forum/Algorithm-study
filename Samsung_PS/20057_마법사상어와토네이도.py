'''

2. 회전 방향 순서 fucn
    서 남 동 북 서 남 동 북 
    [1  1  2  2  3  3  4 4 5 5 6 6 6]
3. 비율 나누는 dict
4. splash_damage 덧셈 func
5. if 나머지 덧셈 func
'''


def pprint(arr):
    for row in arr:
        print(row)
    print()
    
    
N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# 서 남 동북 
splash_dic = {0: [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.01), (1, 1, 0.01), (2, 0, 0.02), (-2, 0, 0.02)],

              1: [(2, 0, 0.05), (1, -1, 0.1), (1, 1, 0.1), (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02)],
              
              2: [(0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02)],
              
              3: [(-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.01), (1, 1, 0.01), (0, -2, 0.02), (0, 2, 0.02)]}


# 서, 남, 동, 북
move_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def shark_move(board):
    result = 0
    idx = 0
    y, x = N//2, N//2
    print()
    pprint(board)
        
    # [1  1  2  2  3  3  4 4 5 5 6 6 6]
    for step in range(1, N): # 나아갈 step 수
        # 마지막인지 아닌지 체크
        repeat_step = 3 if step == N - 1 else 2
        
        # 반복 이동
        for _ in range(repeat_step):
            # 나아갈 방향 선정
            idx %= 4
            dy, dx = move_list[idx]
            
            # step 수만큼 계속 이동
            for _ in range(step):
                y += dy
                x += dx
                result += splash(board, y, x, idx)
                pprint(board)
            idx += 1
            
    return result


def splash(board, y, x, news):
    sand, board[y][x] = board[y][x], 0
    total_damage = 0
    out_sand = 0

    # dict splash 위치
    for dy, dx, damage, in splash_dic[news]:
        ny = y + dy
        nx = x + dx
        spalsh_damge = int(sand*damage)
        total_damage += spalsh_damge
        
        if N > ny >= 0 and N > nx >= 0:
            board[ny][nx] += spalsh_damge
        else:
            out_sand += spalsh_damge
            
    else: # a를 결정
        dy, dx = move_list[news]
        ny = y + dy
        nx = x + dx
        
        if N > ny >= 0 and N > nx >= 0:
            board[ny][nx] += (sand - total_damage)
        else:
            out_sand += (sand - total_damage)
    
    return out_sand


answer = shark_move(board)
print(answer)
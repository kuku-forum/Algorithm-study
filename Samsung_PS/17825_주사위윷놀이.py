# cur_pos에서 next_pos로 이동하는 board 생성
# 현재 나가 0이면 1번으로 간다, 현재 내가 5이면 6과 21 두가지 방향이 존재한다.
board = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18], [19], [20], 
         [32], 
         [22], [23], [24], [30], 
         [26], [24], 
         [28], [29], [24], 
         [31], [20], [32]]

#           1, 2, 3, 4, 5,  6,  7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32      
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]


def play(order, player, result):
    global answer
    
    if order == 10:
        answer = max(answer, result)
        return
    
    for horse in range(4):
        
        cur_pos = player[horse]
        move = dice_list[order]
        
        if len(board[cur_pos]) == 2:
            next_pos = board[cur_pos][1]
        else:
            next_pos = board[cur_pos][0]
            
        for _ in range(1, move):
            next_pos = board[next_pos][0]
        
        if next_pos == 32 or (32 > next_pos and next_pos not in player):
            player[horse] = next_pos
            play(order + 1, player, result + score[next_pos])
            player[horse] = cur_pos
            
    return


dice_list = list(map(int, input().split()))
player = [0, 0, 0, 0]
answer = -1
order = 0
result = 0

play(order, player, result)
print(answer)

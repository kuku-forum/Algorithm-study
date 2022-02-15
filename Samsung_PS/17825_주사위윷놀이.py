'''
처음에는 시작 칸에 말 4개
> 말이 파란색 칸에서 이동을 시작하면 파란색 화살표
> 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표
>  말이 도착 칸으로 이동하면 주사위에 나온 수와 관계 없이 이동을 마친다
> 10개의 턴, 매 턴마다 1부터 5까지 한 면에 하나씩 적혀있는 5면체 주사위를 굴리고, 도착 칸에 있지 않은 말을 하나 골라 주사위에 나온 수만큼 이동
> 말이 이동을 마치는 칸에 다른 말이 있으면 그 말은 고를 수 없다. 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
> 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가

구현 방법
1. map 만들기 
처음> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]
파랑(idx 5)> [13, 16, 19] (idx 9)
파랑(idx 10)> [22, 24] (idx 13)
파랑(idx 15)> [28, 27, 26] (idx 19)
통합 > [25, 30, 35, 40, 0]
'''

# dice_list = list(map(int, input().split()))

player_dic = {0: (0, 'ori'), 1: (0, 'ori'), 2: (0, 'ori'), 3: (0, 'ori')}

board_dic = {
            'ori' : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38],
            'b5' : [0, 13, 16, 19, 25],
            'b10' : [0, 22, 24, 25],
            'b15' : [0, 30, 28, 27, 26, 25],
            'cross' : [0, 30, 35],
            'final' : [0]
            }

def play(order):
    for i, dice in enumerate(dice_list):
        order[i]
        
    return

dice_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
player_dic = {0: (0, 'ori'), 1: (0, 'ori'), 2: (0, 'ori'), 3: (0, 'ori')}


def dupli_chk():
    for i in range(4):
        if id != i and player_pos + step == player_dic[i][0]:
            return True

def move(id, dice_idx):
    
    step = dice_list[dice_idx]
    player_pos = player_dic[id][0]
    
    
    stage = player_dic[id][1]
    
    if stage == 'ori':
        next_pos = player_pos + step
        
        if next_pos == 5:
            player_dic[id][0] = 0
            player_dic[id][1] = 'b5'
            score += 10
        
        elif next_pos == 10:
            player_dic[id][0] = 0
            player_dic[id][1] = 'b10'
            score += 20
            
        elif next_pos == 15:
            player_dic[id][0] = 0
            player_dic[id][1] = 'b15'
            score += 30
        
        elif next_pos <= 19:
            player_dic[id][0] = next_pos
            score += board_dic[stage][next_pos]
            
        elif next_pos == 20:
            player_dic[id][0] = 0
            player_dic[id][1] = 'final'
            score += 40
            
        elif next_pos > 20:
            player_dic[id][0] = -1
            player_dic[id][1] = 'none'
            
            
    elif stage == 'b5':
        next_pos = player_pos + step
        
        if next_pos == 4:
            player_dic[id][0] = 0
            player_dic[id][1] = 'cross'
            score += 25
        
        elif 6 >= next_pos > 4:
            next_pos -= 4
            player_dic[id][0] = next_pos
            player_dic[id][1] = 'cross'
            score += board_dic[stage][next_pos]
            
        elif next_pos == 7:
            player_dic[id][0] = 0
            player_dic[id][1] = 'final'
            score += 40
            
        elif next_pos > 7:
            player_dic[id][0] = -1
            player_dic[id][1] = 'none'
            
        else:
            player_dic[id][0] = next_pos
            score += board_dic[stage][next_pos]
            
        
    elif stage == 'b10':
        next_pos = player_pos + step
        
        if 3 > next_pos:
            player_dic[id][0] = next_pos
            score += board_dic[stage][next_pos]
            
        elif next_pos == 3:
            player_dic[id][0] = 0
            player_dic[id][1] = 'cross'
            score += 25
            
        elif 5 >= next_pos > 3:
            next_pos -= 3
            player_dic[id][0] = next_pos
            player_dic[id][1] = 'cross'
            score += board_dic[stage][next_pos]
            
        elif next_pos == 6:
            player_dic[id][0] = 0
            player_dic[id][1] = 'final'
            score += 40
            
        elif next_pos == 7:
            player_dic[id][0] = -1
            player_dic[id][1] = 'none'
        
        
        
    elif stage == 'b15':
        next_pos = player_pos + step
        
        if next_pos == 4:
            player_dic[id][0] = 0
            player_dic[id][1] = 'cross'
            score += 25
        
        elif 6 >= next_pos > 4:
            next_pos -= 4
            player_dic[id][0] = next_pos
            player_dic[id][1] = 'cross'
            score += board_dic[stage][next_pos]
            
        elif next_pos == 7:
            player_dic[id][0] = 0
            player_dic[id][1] = 'final'
            score += 40
            
        elif next_pos > 7:
            player_dic[id][0] = -1
            player_dic[id][1] = 'none'
            
        else:
            player_dic[id][0] = next_pos
            score += board_dic[stage][next_pos]
            
        
    elif stage == 'cross':
        next_pos = player_pos + step
        
        if next_pos == 3:
            player_dic[id][0] = 0
            player_dic[id][1] = 'final'
            score += 40
            
        if next_pos > 3:
            player_dic[id][0] = -1
            player_dic[id][1] = 'none'
            
        else:
            player_dic[id][0] = next_pos
            score += board_dic[stage][next_pos]
            
        
    elif stage == 'final':
        player_dic[id][0] = -1
        player_dic[id][1] = 'none'
            
        
    
    return False

def recur_idx(id, n, idx):
    
    if n == 3: 
        idx = 0
        return
    
    print(id, n, idx)
    cnt += 1
    # if move():
    #     return
    
    recur_idx(0, n + 1, idx)
    recur_idx(1, n + 1, idx)
    recur_idx(2, n + 1, idx)
    recur_idx(3, n + 1, idx)
    
    return
        
idx = 0
for id in range(4):
    recur_idx(id, 0, idx)


# 각 세대의 pos list 몇 idx 힘들었다.

def dragon_curve(idx, gen):    
    # 동 북 서 남
    ESWN = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    move_list = [idx]
    pos = [(0, 0)]
    pos.append((pos[0][0] + ESWN[idx][0], pos[0][1] + ESWN[idx][1]))
    # (0, 0) (0, 1) (-1, 1) (-1, 0) [-2, 0] (-2, -1) (-1, -1) (-1, -2) (-2, -2)
    # 동     북       서      북             서         남          서         북
    
    for _ in range(gen):
        dragon_len = len(pos)
        
        for i in range(dragon_len - 2, -1, -1):
            next_step = (move_list[i] + 1)%4
            move_list.append(next_step)
            pos.append((pos[-1][0] + ESWN[next_step][0], pos[-1][1] + ESWN[next_step][1]))
    
    return pos



def conv():
    square = [(0, 0), (0, 1), (1, 0), (1, 1)]
    result = 0
    
    for y in range(100):
        for x in range(100):
            
            for dy, dx in square:
                ny = y + dy
                nx = x + dx
                if board[ny][nx] == 0:
                    break
            else:
                result += 1
    
    return result


def matching_pos(y, x, pos):
    
    for dy, dx in pos:
        board[y + dy][x + dx] = 1



N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_pos = dragon_curve(d, g)
    # (0, 0) (0, 1) (-1, 1) (-1, 0) [-2, 0] (-2, -1) (-1, -1) (-1, -2) (-2, -2)
    # x, y -> 3, 3
    # 
    matching_pos(y, x, dragon_pos)
    
answer = conv()
print(answer)
    
C, R = map(int, input().split())
K = int(input())

# 북 동 남 서
direct_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
seat_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

board = [[0 for _ in range(C)] for _ in range(R)]

direct = 0
y_idx = R - 1
x_idx = 0
board[y_idx][x_idx] = 1

seat = [1, 1]
switch = 0
cnt = 1

while K > cnt:
    dy, dx = direct_list[direct]
    sx, sy = seat_list[direct]
    
    if switch%2 == 0:
        
        if switch != 2:
            R -= 1
        
        for _ in range(R):
            cnt += 1
            y_idx += dy
            x_idx += dx
            board[y_idx][x_idx] = cnt
            seat[0] += sx
            seat[1] += sy
            
            if cnt == K:
                break
            
    else:
        C -= 1
        for _ in range(C):
            cnt += 1
            y_idx += dy
            x_idx += dx
            board[y_idx][x_idx] = cnt
            seat[0] += sx
            seat[1] += sy
            
            if cnt == K:
                break
    
    if R == 0 or C == 0:
        answer = 0
        break
        
    switch += 1
    direct = (direct + 1)%4
    
else:    
    answer = ' '.join(map(str, seat))

print(answer)
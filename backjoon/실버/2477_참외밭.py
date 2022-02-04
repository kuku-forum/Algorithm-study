from collections import deque

N = int(input())
que = deque([])

east_cnt = 0
west_cnt = 0
south_cnt = 0
north_cnt = 0


for _ in range(6):
    direct, num = map(int, input().split())
    
    if direct == 1:
        east_cnt += 1
        
    elif direct == 2:
        west_cnt += 1
        
    elif direct == 3:
        south_cnt += 1
        
    elif direct == 4:
        north_cnt += 1
    
    que.append([direct, num])
    
answer = 0


if east_cnt == 2 and west_cnt == 1 and south_cnt == 2 and north_cnt == 1:

    while True:
        if que[0][0] == 4 and que[1][0] == 2 and que[2][0] == 3:
            answer = que[0][1] * que[1][1] - que[3][1] * que[4][1]
            break
        else:
            que.rotate(1)
        
        
elif east_cnt == 1 and west_cnt == 2 and south_cnt == 2 and north_cnt == 1:
    while True:
        if que[0][0] == 4 and que[1][0] == 2 and que[2][0] == 3:
            answer = que[0][1] * que[-1][1] - que[2][1] * que[3][1]
            break
        else:
            que.rotate(1)
    
    
elif east_cnt == 2 and west_cnt == 1 and south_cnt == 1 and north_cnt == 2:
    while True:
        if que[0][0] == 4 and que[1][0] == 2 and que[2][0] == 3:
            answer = que[1][1] * que[2][1] - que[4][1] * que[5][1]
            break
        else:
            que.rotate(1)


elif east_cnt == 1 and west_cnt == 2 and south_cnt == 1 and north_cnt == 2:
    while True:
        if que[0][0] == 4 and que[1][0] == 2 and que[2][0] == 4:
            answer = que[-1][1] * que[-2][1] - que[2][1] * que[1][1]
            break
        else:
            que.rotate(1)

print(answer*N)
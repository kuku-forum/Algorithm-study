'''
108ms, 100/1025

조건
> 0 북, 1 동, 2 남, 3 서
> 빈 칸 0, 벽 1
> (네 방향 모두 청소 or 모두 벽) and 후진도 못하면 끝

1. 현재위치 청소(청소하면 2)
2. 왼쪽 방향 확인 (direct + 3)%4
3_1. 왼쪽 0이면 왼쪽 회전 및 전진(방향 값 및 위치 바꿈)
3_2. 왼쪽이 청소했거나, 벽이면 회전만 진행(현재 방향 값만 바꿈)
3_3. (네 방향 모두 청소 or 모두 벽), 방향값 그대로 뒤로 1보 후진
3_4. (네 방향 모두 청소 or 모두 벽) and 후진x -> 스탑
'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

direct_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
board[r][c] = 2
answer = 1

    
def clean(r, c, d, answer):
    y, x = r, c
    # 왼쪽 방향 (d + 3) % 4
    nd = (d + 3) % 4
    dy, dx = direct_list[nd]
    
    # 왼쪽 청소 안됨, 방향/위치 변경, 청소했으니 2로 변경 및 answer + 1 진행
    if board[y + dy][x + dx] == 0:
        board[y + dy][x + dx] = 2
        y += dy
        x += dx
        d = nd
        answer += 1
    
    # 왼쪽이 벽이거나 청소 됨
    elif board[y + dy][x + dx] > 0:
        
        # 모든 방향 다 탐색, 청소 안한 공간이 있으면 break
        clean_flag = False
        for dy, dx in direct_list:
            
            # 청소할 공간이 있다면 clean_flag 작동
            if board[y + dy][x + dx] == 0:
                clean_flag = True
                break
        else:
            # 모든 방향이 벽이거나 청소 되었으면, 후진 확인
            # 후진 방향 (d + 2) % 4
            nd = (d + 2) % 4
            dy, dx = direct_list[nd]
            
            # 벽이라 후진이 불가능하면 종료
            if board[y + dy][x + dx] == 1:
                return y, x, d, answer, True
            
            # 벽이 아니라면 1보 후진
            else:
                y += dy
                x += dx

        # 모든 방향 중에 청소 할 공간이 있으면 방향만 변경
        if clean_flag:
            d = nd
    
    return y, x, d, answer, False

while True:
    r, c, d, answer, stop = clean(r, c, d, answer)
    if stop: break
    
print(answer)
# 반시계 방향으로 회전하며 확인하는 dict
cleaner = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
# 방향에 따른 후진 방향을 주는 dict
back_dir = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
cnt = 1
N, M = map(int, input().split())
r, c, direction = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[r][c] = -1

while True:
    
    # 반시계 방향으로 회전하며 청소가 안된 곳(0)이 있는지 조사를 진행한다.
    for _ in range(4):
        direction = (direction - 1) % 4
        j, i = cleaner[direction]
        nj, ni = r + j, c + i
        
        # 회전 했을 때, 0이면 cnt를 1증가 시키고 위치를 이동하고 다시 while문을 실행
        if not arr[nj][ni]:
            cnt += 1
            r, c = nj, ni
            arr[r][c] = -1
            break
    # 회전을 다해도 0이 없으면 후진 하는데, 벽이면 while을 나오고 아니면 이동 후 while문 실행
    else:
        j, i = back_dir[direction]
        
        if arr[r + j][c + i] == 1:
            break
        else:
            r, c = r + j, c + i
print(cnt)
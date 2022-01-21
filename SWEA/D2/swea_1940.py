T = int(input())
 
for t in range(1,1+T):
    N = int(input())
    
    # 커맨드, 속도
    command = [list(map(int,input().split())) for _ in range(N)]
 
    # 초기 스피드, 이동 거리
    speed, distance = 0, 0
 
    for com in command:
        
        if com[0] == 1:
            speed += com[1]
 
        elif com[0] == 2:
            speed -= com[1]
            if speed < 0:
                speed = 0
 
        # 이동 거리에 speed 더하기
        # 매초 이동하기 때문에 speed * 1 해줄 필요 없음
        distance += speed
 
    print(f'#{t} {distance}')
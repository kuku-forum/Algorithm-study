'''
속도
> 148ms
> 560명 중에 300등

조건
> N극은 0, S극은 1
> 방향 1: 시계, 방향 -1: 반시계
> 서로 맞닿은 톱니의 극이 다르다면 반대방향
> 서로 맞닿은 톱니의 극이 같으면 그대로
 
점수
> 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
> 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
> 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
> 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점

구현
0. 용이한 회전을 위해 deque로 톱니를 설정
1. command에 따라 각 톱니바퀴가 어디로 회전할지 order 리스트에 설정
2. 모든 톱니바퀴의 회전이 확인되면, order에 명신된 대로 하나씩 rotate를 통해 회전
3. 12시 방향의 톱니를 통해 계산
'''

from collections import deque

wheel = []
command = []

# 4개의 톱니바퀴를 deque로 받음
for _ in range(4):
    info = deque((map(int, list(input()))))
    wheel.append(info)

K = int(input())

# K계의 command(명령)을 받음
for _ in range(K):
    command.append(list(map(int, input().split())))

# 모든 톱니의 idx:2 는 idx:-2와 맞물려 있음
for num, rotate in command:
    
    # 톱니가 돌아갈 순서 선정 몇번 바퀴가 어떻게 돌아갈것인지 저장
    order = [0 for _ in range(4)]
    order[num-1] = rotate

    # 1번 톱니바퀴에게 명령이 내려질 경우
    if num-1 == 0:
        # 1번 톱니바퀴와 2번 톱니바퀴의 맞물린 부분 검사, 극이 다르면 -rotate
        if wheel[0][2] != wheel[1][-2]:
            order[1] = -rotate

        # 2번 톱니바퀴와 3번 톱니바퀴의 맞물린 부분 검사, 극이 다르면 -rotate
        if wheel[1][2] != wheel[2][-2] and order[1] != 0:
            order[2] = -order[1]

        # 3번 톱니바퀴와 4번 톱니바퀴의 맞물린 부분 검사, 극이 다르면 -rotate
        if wheel[2][2] != wheel[3][-2] and order[2] != 0:
            order[3] = -order[2]

    # 2번 톱니바퀴에게 명령이 내려질 경우
    elif num-1 == 1:
        if wheel[1][-2] != wheel[0][2]:
            order[0] = -rotate

        if wheel[1][2] != wheel[2][-2]:
            order[2] = -rotate

        if wheel[2][2] != wheel[3][-2] and order[2] != 0:
            order[3] = -order[2]

    # 3번 톱니바퀴에게 명령이 내려질 경우
    elif num-1 == 2:
        if wheel[2][-2] != wheel[1][2]:
            order[1] = -rotate

        if wheel[1][-2] != wheel[0][2] and order[1] != 0:
            order[0] = -order[1]

        if wheel[2][2] != wheel[3][-2]:
            order[3] = -rotate

    # 4번 톱니바퀴에게 명령이 내려질 경우
    elif num-1 == 3:
        if wheel[3][-2] != wheel[2][2]:
            order[2] = -rotate

        if wheel[2][-2] != wheel[1][2] and order[2] != 0:
            order[1] = -order[2]

        if wheel[1][-2] != wheel[0][2] and order[1] != 0:
            order[0] = -order[1]

    # order에 따라 회전 결정
    # 회전은 deque의 rotate를 통해 진행
    # rotate = 1 -> 모든 idx가 1씩 증가(오른쪽으로 한칸씩 이동)
    # rotate = -1 -> 모든 idx가 1씩 감소(왼쪽으로 한칸씩 이동)
    for i, rot in enumerate(order):
        wheel[i].rotate(rot)

# command의 모든 과정이 끝난후 점수 계산
answer = sum([factor[0]*(2**i) for i, factor in enumerate(wheel)])
print(answer)
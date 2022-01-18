'''
톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
 N극은 0, S극은 1
'''

from collections import deque

wheel = []
command = []

for _ in range(4):
    info = deque((map(int, list(input()))))
    wheel.append(info)

K = int(input())

for _ in range(K):
    command.append(list(map(int, input().split())))

# print(wheel)
for num, rotate in command:
    order = [0 for _ in range(4)]
    order[num-1] = rotate

    if num-1 == 0:
        if wheel[0][2] != wheel[1][-2]:
            order[1] = -rotate

        if wheel[1][2] != wheel[2][-2] and order[1] != 0:
            order[2] = -order[1]

        if wheel[2][2] != wheel[3][-2] and order[2] != 0:
            order[3] = -order[2]

    elif num-1 == 1:
        if wheel[1][-2] != wheel[0][2]:
            order[0] = -rotate

        if wheel[1][2] != wheel[2][-2]:
            order[2] = -rotate

        if wheel[2][2] != wheel[3][-2] and order[2] != 0:
            order[3] = -order[2]

    elif num-1 == 2:
        if wheel[2][-2] != wheel[1][2]:
            order[1] = -rotate

        if wheel[1][-2] != wheel[0][2] and order[1] != 0:
            order[0] = -order[1]

        if wheel[2][2] != wheel[3][-2]:
            order[3] = -rotate

    elif num-1 == 3:
        if wheel[3][-2] != wheel[2][2]:
            order[2] = -rotate

        if wheel[2][-2] != wheel[1][2] and order[2] != 0:
            order[1] = -order[2]

        if wheel[1][-2] != wheel[0][2] and order[1] != 0:
            order[0] = -order[1]

    for i, rot in enumerate(order):
        wheel[i].rotate(rot)

answer = sum([factor[0]*(2**i) for i, factor in enumerate(wheel)])
print(answer)
import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
    
    command_list = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    if n > 0:
        que = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    else:
        tmp = sys.stdin.readline()
        que = deque()

    trigger = True
    cnt = 0

    for command in command_list:
        if command == 'R':
            cnt += 1
            
        elif command == 'D':
            if not que:
                print('error')
                trigger = False
                break
            elif cnt % 2 == 1:
                que.pop()
            else:
                que.popleft()
            
    
    if trigger and cnt%2==1:
        que.reverse()
        print('[', ','.join(que), ']', sep='')
    elif trigger and cnt%2 == 0:
        print('[', ','.join(que), ']', sep='')



# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# for _ in range(N):
#     T = sys.stdin.readline().rstrip()
#     command_list = []
#     cnt = 0 

#     for i in range(len(T)):
#         if T[i] == 'D':
#             if cnt % 2 == 1:
#                 command_list.append('R')
#             command_list.append(T[i])
#             cnt = 0
#         else:
#             cnt += 1

#     n = int(sys.stdin.readline())
#     if n > 0:
#         que = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
#     else:
#         tmp = sys.stdin.readline()
#         que = deque()

#     trigger = True

#     for command in command_list:
#         if command == 'R':
#             que.reverse()
#         elif command == 'D':
#             if not que:
#                 print('error')
#                 trigger = False
#                 break
#             que.popleft()
    
#     if trigger:
#         print('[', ','.join(que), ']', sep='')
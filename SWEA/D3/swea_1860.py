from my_package.hjtc import swea_tc

from collections import deque

T = int(input())

for t in range(1, T + 1):
    answer = 'Impossible'
    
    N, M, K = map(int, input().split())
    que = deque(sorted(map(int, input().split())))
    # print(que)
    
    bread = 0
    cnt = 0
    flag = False
    if que[0] == 0:
        swea_tc(f'#{t} {answer}')
    else:
        while que:
            cnt += 1
            
            if cnt % M == 0:
                bread += K

            while que and cnt == que[0]:
                if bread > 0:
                    bread -= 1
                    que.popleft()
                else:
                    flag = True
                    break
            if flag:
                break
            
            
        else:
            answer = 'Possible'
    
        
        swea_tc(f'#{t} {answer}')
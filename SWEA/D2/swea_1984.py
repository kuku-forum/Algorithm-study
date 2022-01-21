from collections import deque

T = int(input())

for t in range(1, T + 1):
    que = deque(sorted(map(int, input().split())))
    que.pop()
    que.popleft()
    
    print(f'#{t} {round(sum(que)/len(que))}')
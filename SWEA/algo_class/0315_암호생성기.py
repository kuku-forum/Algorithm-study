from my_package.hjtc import swea_tc as print

from collections import deque


def solution(que):
    
    while True:
        for i in range(1, 6):
            num = que.popleft() - i
            
            if 0 >= num:
                num = 0
                
            que.append(num)
            
            if que[-1] == 0:
              return que
    
    
for t in range(1, 11):
    _ = input()
    arr = deque(map(int, input().split()))

    print(f'#{t} {" ".join(map(str, solution(arr)))}')
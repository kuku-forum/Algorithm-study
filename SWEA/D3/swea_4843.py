from collections import deque

T = int(input())

for t in range(1, T + 1):
    input()
    arr = deque(sorted(list(map(int, input().split()))))
    answer = []
    
    while arr:
        answer.append(arr.pop())
        if not arr: break
        answer.append(arr.popleft())
    
    answer_str = ' '.join(map(str, answer[:10]))
    print(f'#{t} {answer_str}')
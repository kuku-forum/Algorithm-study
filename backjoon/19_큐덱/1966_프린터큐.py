import sys
from collections import deque

cnt = int(sys.stdin.readline())

N, M, W = [], [], []

for _ in range(cnt):
    n, m = map(int, sys.stdin.readline().split())
    N.append(n)
    M.append(m)
    W.append(deque(map(int, sys.stdin.readline().split())))


for idx in range(cnt):
    
    T_N = N[idx]
    T_M = M[idx]
    T_W = W[idx]
    idx_list = deque([i for i in range(T_N)])
    answer = 0

    while True:
        if T_W[0] == max(T_W):
            T_W.popleft()
            answer += 1

            if idx_list.popleft() == T_M:
                print(answer)
                break
        
        else:
            T_W.append(T_W.popleft())
            idx_list.append(idx_list.popleft())
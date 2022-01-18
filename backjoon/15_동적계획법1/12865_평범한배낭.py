import sys

N, K = map(int, sys.stdin.readline().split())
value_map = [[0 for _ in range(K+1)] for _ in range(N+1)]

W_list, V_list = [0], [0]
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    W_list.append(W)
    V_list.append(V)

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= W_list[i]:
            value_map[i][j] = max(value_map[i-1][j], value_map[i-1][j-W_list[i]] + V_list[i])
        else:
            value_map[i][j] = value_map[i-1][j]
        
print(value_map[-1][-1])
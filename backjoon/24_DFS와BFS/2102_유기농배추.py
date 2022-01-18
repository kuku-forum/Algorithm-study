import sys
from collections import deque

T = int(sys.stdin.readline())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(graph, m, n): # m : 가로길이, n : 세로길이
    visited = []
    que = deque()
    cnt = 0

    for y in range(n):
        for x in range(m):
            cnt_trigger = False

            if not que: que.append((x, y))
            
            while que:
                node = que.popleft()

                if node in graph and node not in visited:
                    visited.append(node)
                    cnt_trigger = True
                    
                    for direct in direction:
                        tmp_x = node[0] + direct[0]
                        tmp_y = node[1] + direct[1]

                        if tmp_y >= 0 and tmp_x >= 0 and n > tmp_y and m > tmp_x:
                            que.append((tmp_x, tmp_y))
            
            if cnt_trigger: cnt += 1

    return cnt


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph_list = []
    
    for _ in range(K):
        graph_list.append(tuple(map(int, sys.stdin.readline().split())))

    print(bfs(graph_list, M, N))
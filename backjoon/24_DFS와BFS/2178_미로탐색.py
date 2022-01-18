import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph_list = []
direct_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for _ in range(N):
    row = sys.stdin.readline().rstrip()
    tmp = []
    for num in row:
        tmp.append(int(num))
    graph_list.append(tmp)


def bfs(graph, root):
    que = deque([root])

    while que:
        node = que.popleft()

        for direct in direct_list:
            new_y = node[0] + direct[0]
            new_x = node[1] + direct[1]

            if N > new_y >= 0 and M > new_x >= 0:
                if new_y == 0 and new_x == 0:
                    continue
                
                if graph[new_y][new_x] == 1:
                    graph[new_y][new_x] = graph[node[0]][node[1]] + 1
                    que.append([new_y, new_x])

    return graph

# print(bfs(graph_list, [0, 0]))
print(bfs(graph_list, [0, 0])[-1][-1])
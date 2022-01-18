import sys
from collections import deque

def bfs(graph, root, goal):
    direct_list = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                    (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    visited = [[-1 for _ in range(graph)] for _ in range(graph)]
    visited[root[0]][root[1]] = 0
    que = deque([root])

    while que:
        y, x = que.popleft()

        if y == goal[0] and x == goal[1]:
            return visited[y][x]

        for direct in direct_list:
            n_y = y + direct[0]
            n_x = x + direct[1]

            if graph > n_y >= 0 and graph > n_x >= 0:
                if visited[n_y][n_x] == -1:
                    visited[n_y][n_x] = visited[y][x] + 1
                    que.append([n_y, n_x])

    return -1


N = int(sys.stdin.readline())

for _ in range(N):
    X = int(sys.stdin.readline())
    start = list(map(int, sys.stdin.readline().split()))
    target = list(map(int, sys.stdin.readline().split()))
    print(bfs(X, start, target))
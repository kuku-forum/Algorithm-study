import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph_list = []

for _ in range(N):
    row = []
    for num in str(sys.stdin.readline().rstrip()):
        row.append(int(num))
    graph_list.append(row)

def bfs(graph, root):

    que = deque([root])
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] 
    # visited = [[[0] * 2 ] * M ] * N # 절대로 이거 쓰면 안됨
    visited[0][0][1] = 1 # (0, 0) 에서 벽을 1개 부슬 수 있다는 의미, 처음 값은 방문 했으니 1로 설정
    direct_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while que:

        y, x, wall = que.popleft()

        if y == N - 1 and x == M - 1:
            return visited[y][x][wall]

        for direct in direct_list:
            n_y = y + direct[0]
            n_x = x + direct[1]   

            if N > n_y >=0 and M > n_x >= 0:
                
                # 벽을 만나고, 벽을 뚫을수 있다면...
                if graph[n_y][n_x] == 1 and wall == 1: 
                    visited[n_y][n_x][0] = visited[y][x][wall] +1 # 벽을 한번 뚫은 상태(0) 에 방문 처리
                    que.append([n_y, n_x, 0]) # 벽을 이제 못 뚫는다는 의미


                # 통로 만났고, 방문하지 않았다면... , 통로를 만났기 때문에 wall의 값은 중요하지 않음
                elif graph[n_y][n_x] == 0 and visited[n_y][n_x][wall] == 0: 

                    visited[n_y][n_x][wall] = visited[y][x][wall] +1 # 방문 처리
                    que.append([n_y, n_x, wall])
    return -1

# 벽 하나를 뚫을 수 있고, (0, 0)에서 시작
print(bfs(graph_list, [0,0,1]))

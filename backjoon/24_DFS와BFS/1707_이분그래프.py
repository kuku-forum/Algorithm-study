import sys
from collections import deque

def bfs(root):

    que = deque([root])
    visited[root] = 1

    while que:
        node = que.popleft()

        # node 주소에 속한 find_node를 찾음
        for find_node in graph_list[node]: 

            # find_node가 방문하지 않을 경우
            if not visited[find_node]:
                
                #  기존 node가 1일 경우 find_node는 2 혹은 그 반대로 설정
                if visited[node] == 1:
                    visited[find_node] = 2
                
                elif visited[node] == 2:
                    visited[find_node] = 1
                
                que.append(find_node)

            # find_node를 방문 하였을 경우 node와 find_node를 비교
            elif visited[node] == visited[find_node]:
                return 'NO'

    return 'YES'


K = int(sys.stdin.readline())
for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph_list = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, sys.stdin.readline().split())
        graph_list[start].append(end)
        graph_list[end].append(start)

    visited = [0 for _ in range(V+1)]

    for i in range(1, V+1):
        if visited[i] == 0:
            answer = bfs(i)

            if answer == 'NO':
                break

    print(answer)
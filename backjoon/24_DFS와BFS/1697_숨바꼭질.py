import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 150000

def bfs(root, target):
    
    que = deque([root])
    dist = [0]*(MAX + 1)

    while que:
        node = que.popleft()
        # print(node)
        if node == target:
            return dist[node]

        for new_node in (node -1, node + 1, node*2):
            if MAX >= new_node >= 0 and not dist[new_node]:
                dist[new_node] = dist[node] + 1

                que.append(new_node)

def dfs(root, target):
    que = [root]
    dist = [0]*(MAX + 1)

    while que:
        node = que.pop()
        # print(node)
        if node == target:
            return dist[node]

        for new_node in (node -1, node + 1, node*2):
            if MAX >= new_node >= 0 and not dist[new_node]:
                dist[new_node] = dist[node] + 1
                que.append(new_node)

print(bfs(N, K))
print(dfs(N, K))
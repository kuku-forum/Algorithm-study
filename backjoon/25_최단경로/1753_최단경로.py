import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = sys.maxsize
graph_list = [[] for _ in range(V+1)]

for _ in range(E):
    s_node, e_node, w = map(int, sys.stdin.readline().split())
    graph_list[s_node].append([e_node, w])

def dijkstra(graph, root):
    dp = [INF for _ in range(V+1)]
    dp[root] = 0
    heap = []
    heapq.heappush(heap, (0, root))

    while heap:
        weight, node = heapq.heappop(heap)

        if dp[node] < weight:
            continue

        for find_node, find_weight in graph[node]:
            sum_weight = weight + find_weight

            if sum_weight < dp[find_node]:
                dp[find_node] = sum_weight
                heapq.heappush(heap, (sum_weight, find_node))
    return dp

answer = dijkstra(graph_list, K)
# print(answer)
for i in range(1, V+1):
    print("INF" if answer[i] == INF else answer[i])
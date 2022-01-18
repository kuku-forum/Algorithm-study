import sys
import heapq

N, E = map(int, sys.stdin.readline().split())
graph_list = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph_list[a].append([b, c])
    graph_list[b].append([a, c])

V1, V2 = map(int, sys.stdin.readline().split())
INF = 0xffff # 0xffff를 써야함 sys.maxsize든 = 등호를 꼭 붙여야함

def dijkstra(graph, start, end, v1, v2):
    sum_dp = []

    for root in (start, v1, v2):
        dp = [INF for _ in range(N+1)]
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
        sum_dp.append(dp)

    tmp1 = sum_dp[0][v1] + sum_dp[1][v2] + sum_dp[2][end]
    tmp2 = sum_dp[0][v2] + sum_dp[2][v1] + sum_dp[1][end]
    result = min(tmp1, tmp2)
    
    return -1 if result >= INF else result # 0xffff를 써야함 sys.maxsize든 = 등호를 꼭 붙여야함

print(dijkstra(graph_list, 1, N, V1, V2))
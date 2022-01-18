import sys
import heapq

T = int(sys.stdin.readline())
INF = sys.maxsize

def dijkstra(graph, t_list, start, v1, v2):
    
    sum_dp = []
    answer = []

    for root in (start, v1, v2):
        dp = [INF for _ in range(n + 1)]
        dp[root] = 0
        heap = []
        heapq.heappush(heap, (0, root))
        # print('#0', heap)

        while heap:
            weight, node = heapq.heappop(heap)
            # print('#1', weight, node)

            if weight > dp[node]:
                continue

            for find_node, find_weight in graph[node]:
                sum_weight = weight + find_weight

                if sum_weight < dp[find_node]:
                    dp[find_node] = sum_weight
                    heapq.heappush(heap, (sum_weight, find_node))
        
        sum_dp.append(dp)
    
    # print(sum_dp)
    for target in t_list:
        s_path = sum_dp[0][target]
        path1 = sum_dp[0][v1] + sum_dp[1][v2] + sum_dp[2][target]
        path2 = sum_dp[0][v2] + sum_dp[2][v1] + sum_dp[1][target]

        # print('#1', s_path, path1, path2 )
        if s_path == min(path1, path2):
            answer.append(target)

    return answer



for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph_list = [[] for _ in range(n+1)]
    target_list = []
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph_list[a].append((b, d))
        graph_list[b].append((a, d))

    for _ in range(t):
        target_list.append(int(sys.stdin.readline()))

    result = dijkstra(graph_list, target_list, s, g, h)
    print(*sorted(result), sep = ' ')
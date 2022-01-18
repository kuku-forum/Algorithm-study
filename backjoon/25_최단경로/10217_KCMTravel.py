import sys
import heapq

T = int(sys.stdin.readline())
INF = sys.maxsize

def kcm(graph, root_node, root_money):
    dist = [[INF for _ in range(M + 1)] for _ in range(N + 1)]

    dist[root_node][root_money] = 0
    
    for money in range(M + 1):
        for node in range(1, N + 1):
            weight = dist[node][money]
            
            if  weight >= INF:
                continue

            for find_node, find_money, find_weight in graph[node]:
                sum_money = find_money + money

                if sum_money > M:
                    continue
                
                dist[find_node][sum_money] = min(dist[find_node][sum_money], weight + find_weight)

    answer = min(dist[N])
    return answer if INF > answer else 'Poor KCM'


for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())    
    graph_list = [[] for _ in range(N + 1)]

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        graph_list[u].append([v, c, d])

    print(kcm(graph_list, 1, 0))


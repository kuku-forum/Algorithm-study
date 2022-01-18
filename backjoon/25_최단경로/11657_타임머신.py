import sys

N, M = map(int, sys.stdin.readline().split())
graph_list = []

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph_list.append((A, B, C))

INF = sys.maxsize

def belman_ford(graph):
    dp = [INF for _ in range(N + 1)]
    dp[1] = 0

    for i in range(N):
        for j in range(M):
            node = graph[j][0]
            next_node = graph[j][1]
            weight = graph[j][2]

            print(i,j, node, next_node, weight)

            if dp[node] != INF and dp[next_node] > dp[node] + weight:
                if i == N -1:
                    print('False', dp[1:])
                    return False

                dp[next_node] = dp[node] + weight

            print(dp)
        print()
    return dp[2:]
    

result = belman_ford(graph_list)
print(result)

if not result:
    print(-1)
else:
    for i in result:
        if i >= INF:
            print(-1)
        else:
            print(i)
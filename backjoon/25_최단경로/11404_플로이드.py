import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = sys.maxsize

graph_list = []

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph_list.append([a, b, c])

def floyd(graph):
    dp = [[INF for _ in range(N)] for _ in range(N)]
    
    for i, j, num in graph:
        if i == j:
            dp[i-1][j-1] = 0
        elif dp[i-1][j-1] > num:
            dp[i-1][j-1] = num
        
    for mid in range(N):
        for start in range(N):
            for end in range(N):
                if start == end:
                    dp[start][end] = 0

                elif dp[start][end] > dp[start][mid] + dp[mid][end]:
                    dp[start][end] = dp[start][mid] + dp[mid][end]
    return dp

graph_floyd = floyd(graph_list)

for row in graph_floyd:
    for factor in row:
        if factor >= INF:
            print(0, end = ' ')
        else:
            print(factor, end = ' ')
    print()
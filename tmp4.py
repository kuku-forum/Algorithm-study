from pprint import pprint
import sys
from itertools import permutations

INF = sys.maxsize
print(INF)
def print_board(arr):
    for row in arr:
        tmp = []
        for f in row:
            if f == INF:
                tmp.append(0)
            else:
                tmp.append(f)
        print(tmp)
    print()
            
def floyd(N, graph):
    
    dp = [[INF for _ in range(N)] for _ in range(N)]
    
    for i, j, num in graph:
        if dp[i-1][j-1] > num:
            dp[i-1][j-1] = num
        
    for mid in range(N):
        for start in range(N):
            for end in range(N):
                if start == end:
                    dp[start][end] = 0

                elif dp[start][end] > dp[start][mid] + dp[mid][end]:
                    dp[start][end] = dp[start][mid] + dp[mid][end]
    return dp

def solution(n, edges):
    answer = 0
    
    graph_list = []
    
    for i, j in edges:
        graph_list.append([i, j, 1])
        graph_list.append([j, i, 1])
    
    board, tmp = floyd(n, graph_list)
    print(tmp)
    print_board(board)
    
    for i, j, k in permutations([idx for idx in range(n)], 3):
        # print(i,j,k)
        if board[i][k] == board[i][j] + board[j][k]:
            answer += 1
    # print(answer)
    return answer



solution(5, [[0, 1], [0, 2], [1, 3], [1, 4]])
solution(4, [[2, 3], [0, 1], [1, 2]])

# for i in range(300000):
#     for i in range(300000):
#         for i in range(300000):
#             'do'
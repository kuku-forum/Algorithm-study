'''
정확성  테스트
테스트 1 〉	통과 (0.08ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.07ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.3MB)
테스트 6 〉	통과 (1.57ms, 10.3MB)
테스트 7 〉	통과 (1.56ms, 10.3MB)
테스트 8 〉	통과 (1.52ms, 10.3MB)
테스트 9 〉	통과 (1.77ms, 10.3MB)
테스트 10 〉	통과 (2.94ms, 10.3MB)
테스트 11 〉	통과 (33.44ms, 10.3MB)
테스트 12 〉	통과 (7.84ms, 10.3MB)
테스트 13 〉	통과 (0.46ms, 10.2MB)
테스트 14 〉	통과 (1.28ms, 10.3MB)
테스트 15 〉	통과 (2.79ms, 10.3MB)
테스트 16 〉	통과 (5.08ms, 10.2MB)
테스트 17 〉	통과 (9.07ms, 10.3MB)
테스트 18 〉	통과 (14.86ms, 10.4MB)
테스트 19 〉	통과 (22.53ms, 10.4MB)
테스트 20 〉	통과 (2.59ms, 10.4MB)
테스트 21 〉	통과 (1.73ms, 10.2MB)
테스트 22 〉	통과 (0.26ms, 10.3MB)
테스트 23 〉	통과 (0.25ms, 10.3MB)
테스트 24 〉	통과 (0.26ms, 10.3MB)
테스트 25 〉	통과 (0.08ms, 10.3MB)
'''
from collections import deque
import sys

def solution(board):
    
    INF = sys.maxsize
    direct_lst = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    corner_lst = [1, 1, -1, -1] # y y x x
    visited = [[[INF, INF, INF, INF] for i in range(len(board[0]))] for _ in range(len(board))]
    
    for i in range(4):
        visited[0][0][i] = 0
    
    que = deque([(0, 0, 0, 0)])
    
    while que:
        y, x, cost, corner = que.popleft()
            
        for i, direct in enumerate(direct_lst):
            n_y = y + direct[0]
            n_x = x + direct[1]
            n_corner = corner_lst[i]
            
            if len(board) > n_y >= 0 and len(board[0]) > n_x >= 0 and board[n_y][n_x] == 0:
                current_cost = cost
                current_cost += 100
                
                if corner != 0 and n_corner != corner:
                    current_cost += 500
                
                if visited[n_y][n_x][i] > current_cost:
                    visited[n_y][n_x][i] = current_cost
                    que.append((n_y, n_x, current_cost, n_corner))
                    
    return min(visited[-1][-1])
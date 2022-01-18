'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.05ms, 10.3MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (0.04ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.08ms, 10.3MB)
테스트 8 〉	통과 (0.11ms, 10.3MB)
테스트 9 〉	통과 (0.07ms, 10.3MB)
테스트 10 〉	통과 (0.14ms, 10.3MB)
테스트 11 〉	통과 (0.06ms, 10.3MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.05ms, 10.3MB)
테스트 14 〉	통과 (0.05ms, 10.3MB)
테스트 15 〉	통과 (0.07ms, 10.3MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.07ms, 10.3MB)
테스트 18 〉	통과 (0.02ms, 10.4MB)
테스트 19 〉	통과 (0.02ms, 10.3MB)
테스트 20 〉	통과 (0.02ms, 10.3MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (14.28ms, 10.4MB)
테스트 2 〉	통과 (4.79ms, 10.4MB)
테스트 3 〉	통과 (10.58ms, 10.4MB)
테스트 4 〉	통과 (7.57ms, 10.4MB)
'''
from collections import deque

def solution(maps):
    que = deque([(0, 0)])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = 1
    drt_lst = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while que:
        y, x = que.popleft()
        
        for drt in drt_lst:
            n_y = y + drt[0]
            n_x = x + drt[1]
            
            if len(maps) > n_y >= 0 and len(maps[0]) > n_x >= 0:
                if maps[n_y][n_x] == 1 and visited[n_y][n_x] == 0:
                    
                    visited[n_y][n_x] = visited[y][x] + 1
                    que.append((n_y, n_x))
    
    if visited[-1][-1] == 0:
        return -1
    else:
        return visited[-1][-1]
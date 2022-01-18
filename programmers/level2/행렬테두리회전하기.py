'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (153.36ms, 11.9MB)
테스트 4 〉	통과 (87.33ms, 11.2MB)
테스트 5 〉	통과 (125.64ms, 11.3MB)
테스트 6 〉	통과 (133.74ms, 12MB)
테스트 7 〉	통과 (205.70ms, 12.1MB)
테스트 8 〉	통과 (96.32ms, 11.4MB)
테스트 9 〉	통과 (160.22ms, 11.8MB)
테스트 10 〉	통과 (102.22ms, 11.4MB)
테스트 11 〉	통과 (117.27ms, 11.3MB)
'''
from collections import deque

def solution(rows, columns, queries):
    answer = []
    board = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    cnt = 1
    
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            board[i][j] = cnt
            cnt += 1
    
    for query in queries:
        s_y, s_x, e_y, e_x = query 
        
        que = deque([])
        for x in range(s_x, e_x): que.append(board[s_y][x])
        for y in range(s_y, e_y): que.append(board[y][e_x])
        for x in range(e_x, s_x, -1): que.append(board[e_y][x])
        for y in range(e_y, s_y, -1): que.append(board[y][s_x])
        
        que.rotate(1)
        answer.append(min(que))
        
        for x in range(s_x, e_x): board[s_y][x] = que.popleft()
        for y in range(s_y, e_y): board[y][e_x] = que.popleft()
        for x in range(e_x, s_x, -1): board[e_y][x] = que.popleft()
        for y in range(e_y, s_y, -1): board[y][s_x] = que.popleft()
    
    return answer
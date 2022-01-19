'''
정확성  테스트
테스트 1 〉	통과 (0.11ms, 10.2MB)
테스트 2 〉	통과 (0.09ms, 10.4MB)
테스트 3 〉	통과 (0.09ms, 10.3MB)
테스트 4 〉	통과 (0.20ms, 10.3MB)
테스트 5 〉	통과 (0.34ms, 10.3MB)
테스트 6 〉	통과 (0.48ms, 10.3MB)
테스트 7 〉	통과 (0.34ms, 10.3MB)
테스트 8 〉	통과 (1.34ms, 10.3MB)
테스트 9 〉	통과 (2.15ms, 10.3MB)
테스트 10 〉	통과 (1.95ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (158.87ms, 10.5MB)
테스트 2 〉	통과 (554.29ms, 11.2MB)
테스트 3 〉	통과 (1295.91ms, 11.5MB)
테스트 4 〉	통과 (1333.87ms, 11.5MB)
테스트 5 〉	통과 (1340.71ms, 11.5MB)
테스트 6 〉	통과 (1329.71ms, 11.5MB)
테스트 7 〉	통과 (1259.47ms, 13.9MB)
테스트 8 〉	통과 (1344.42ms, 14.1MB)
테스트 9 〉	통과 (1384.65ms, 12.9MB)
테스트 10 〉	통과 (1419.52ms, 13MB)
테스트 11 〉	통과 (1410.31ms, 12.9MB)
테스트 12 〉	통과 (1329.92ms, 12.7MB)
테스트 13 〉	통과 (1264.79ms, 12.9MB)
테스트 14 〉	통과 (1250.56ms, 12.8MB)
테스트 15 〉	통과 (1386.58ms, 12.9MB)
테스트 16 〉	통과 (1332.57ms, 11.5MB)
테스트 17 〉	통과 (1219.80ms, 11.4MB)
테스트 18 〉	통과 (1292.63ms, 11.3MB)
테스트 19 〉	통과 (1302.79ms, 11.5MB)
테스트 20 〉	통과 (1337.47ms, 11.8MB)
테스트 21 〉	통과 (1305.58ms, 11.8MB)
테스트 22 〉	통과 (1329.54ms, 12.9MB)
테스트 23 〉	통과 (1262.24ms, 12.8MB)
테스트 24 〉	통과 (1256.66ms, 12.9MB)
테스트 25 〉	통과 (1321.10ms, 11.3MB)
테스트 26 〉	통과 (1316.75ms, 10.9MB)
테스트 27 〉	통과 (1143.45ms, 10.6MB)
테스트 28 〉	통과 (1228.37ms, 10.5MB)
테스트 29 〉	통과 (168.28ms, 10.5MB)
테스트 30 〉	통과 (165.86ms, 10.3MB)
'''
INF = 0xffff
def solution(n, s, a, b, fares):
    INF = n*100000
    answer = INF
    board = [[INF for _ in range(n)] for _ in range(n)]
    
    for start, end, cost in fares:
        board[start-1][end-1] = min(INF, cost)
        board[end-1][start-1] = min(INF, cost)
        
    
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if start == end:
                    board[start][end] = 0
                    continue
                    
                if board[start][end] > board[start][mid] + board[mid][end]:
                    board[start][end] = board[start][mid] + board[mid][end]
    
    for mid in range(n):
        mid_cost = board[s-1][mid]
        a_cost = board[mid][a-1]
        b_cost = board[mid][b-1]
        answer = min(answer, mid_cost + a_cost + b_cost)
    
    return answer

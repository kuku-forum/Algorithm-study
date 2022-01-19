
'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.3MB)
테스트 2 〉	통과 (0.15ms, 10.3MB)
테스트 3 〉	통과 (0.15ms, 10.3MB)
테스트 4 〉	통과 (1.32ms, 10.3MB)
테스트 5 〉	통과 (2.09ms, 10.3MB)
테스트 6 〉	통과 (5.14ms, 10.3MB)
테스트 7 〉	통과 (29.12ms, 10.4MB)
테스트 8 〉	통과 (48.67ms, 10.5MB)
테스트 9 〉	통과 (60.86ms, 10.6MB)
테스트 10 〉	통과 (56.02ms, 10.7MB)
'''
from pprint import pprint
from collections import Counter

def solution(n, results):
    answer = 0
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for win, lose in results:
        dp[win-1][lose-1] += 1
        dp[lose-1][win-1] -= 1
    pprint(dp)
    print()
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                
                if dp[start][end] == 0:
                    
                    if dp[start][mid] == 1 and dp[mid][end] == 1:
                        dp[start][end] += 1
                        
                    elif dp[start][mid] == -1 and dp[mid][end] == -1:
                        dp[start][end] += -1
    
    pprint(dp)
    for i in range(n):
        if Counter(dp[i])[0] == 1:
            answer += 1
    
    return answer
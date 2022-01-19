'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.2MB)
테스트 11 〉	통과 (0.36ms, 10.4MB)
테스트 12 〉	통과 (0.33ms, 10.3MB)
테스트 13 〉	통과 (0.18ms, 10.3MB)
테스트 14 〉	통과 (0.48ms, 10.3MB)
테스트 15 〉	통과 (0.36ms, 10.3MB)
테스트 16 〉	통과 (0.39ms, 10.3MB)
'''
def solution(n):
    
    dp = [0, 1, 2]
    
    for i in range(3, n+1):
        dp.append(dp[i-1] + dp[i-2])
    
    return dp[n]%1234567
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.4MB)
테스트 5 〉	통과 (0.06ms, 10.1MB)
테스트 6 〉	통과 (0.06ms, 10.4MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (0.11ms, 10.2MB)
테스트 9 〉	통과 (0.06ms, 10.2MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (4.36ms, 10.3MB)
테스트 2 〉	통과 (1.38ms, 10.4MB)
테스트 3 〉	통과 (2.19ms, 10.3MB)
테스트 4 〉	통과 (2.45ms, 10.3MB)
테스트 5 〉	통과 (1.84ms, 10.2MB)
테스트 6 〉	통과 (3.40ms, 10.3MB)
테스트 7 〉	통과 (1.64ms, 10.2MB)
테스트 8 〉	통과 (3.13ms, 10.3MB)
테스트 9 〉	통과 (3.58ms, 10.3MB)
테스트 10 〉	통과 (1.94ms, 10.2MB)
'''
def solution(m, n, puddles):
    
    puddles = [[q,p] for [p,q] in puddles]      # 미리 puddles 좌표 거꾸로
    dp = [[0] * (m + 1) for i in range(n + 1)]  # dp 초기화
    dp[1][1] = 1           # 집의 위치(시작위치)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [i, j] in puddles:    # 웅덩이 위치의 경우 값을 0으로
                dp[i][j] = 0
            else:                    # 현재 칸은 왼쪽 칸, 위 칸의 합산!
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]

'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.1MB)
테스트 2 〉	통과 (0.17ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.1MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.11ms, 10.2MB)
테스트 8 〉	통과 (0.07ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.23ms, 10.2MB)
테스트 11 〉	통과 (0.23ms, 10.1MB)
테스트 12 〉	통과 (0.14ms, 10.2MB)
테스트 13 〉	통과 (0.15ms, 10.1MB)
테스트 14 〉	통과 (0.11ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (3.73ms, 10.1MB)
테스트 2 〉	통과 (1.94ms, 10.1MB)
테스트 3 〉	통과 (2.68ms, 10.1MB)
테스트 4 〉	통과 (2.70ms, 10.2MB)
테스트 5 〉	통과 (2.60ms, 10.1MB)
테스트 6 〉	통과 (3.10ms, 10.1MB)
'''
def solution(n):
    answer = 1
    s_n = n//2 + 1
    tig = False
    
    while True:
        tmp = 0
        
        for i in range(s_n, 0, -1):
            tmp += i
            
            if tmp == n:
                answer += 1
                s_n -= 1
                break
                
            elif tmp > n:
                s_n -= 1
                break
        else:
            tig = True
            break
        
        if tig:
            break
        
    return answer

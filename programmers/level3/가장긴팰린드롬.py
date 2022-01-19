'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.09ms, 10.2MB)
테스트 4 〉	통과 (0.09ms, 10.2MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.08ms, 10.2MB)
테스트 7 〉	통과 (0.07ms, 10.2MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (0.24ms, 10.2MB)
테스트 10 〉	통과 (0.15ms, 10.2MB)
테스트 11 〉	통과 (0.37ms, 10.2MB)
테스트 12 〉	통과 (0.82ms, 10.3MB)
테스트 13 〉	통과 (0.07ms, 10.2MB)
테스트 14 〉	통과 (0.15ms, 10.2MB)
테스트 15 〉	통과 (0.15ms, 10.2MB)
테스트 16 〉	통과 (0.17ms, 10.2MB)
테스트 17 〉	통과 (0.00ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.4MB)
테스트 19 〉	통과 (0.07ms, 10.2MB)
테스트 20 〉	통과 (0.19ms, 10.2MB)
테스트 21 〉	통과 (0.22ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (3.21ms, 10.3MB)
테스트 2 〉	통과 (299.91ms, 10.1MB)
'''
def solution(s):
    answer = 1
    
    for i in range(len(s)):
        left, right = i-1, i+1
        odd_length = 1
        
        # odd
        while left >= 0 and len(s) > right:
            if s[left] == s[right]:
                odd_length += 2
                left -= 1
                right += 1
            else:
                answer = max(answer, odd_length)
                break
        else:
            answer = max(answer, odd_length)
            
        # even
        left, right = i, i+1
        even_length = 0
        
        while left >= 0 and len(s) > right:
            if s[left] == s[right]:
                even_length += 2
                left -= 1
                right += 1
            else:
                answer = max(answer, even_length)
                break
        else:
            answer = max(answer, even_length)
            
    return answer
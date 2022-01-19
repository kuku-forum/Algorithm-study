'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.12ms, 10.2MB)
테스트 4 〉	통과 (11.39ms, 14.3MB)
테스트 5 〉	통과 (60.28ms, 31.7MB)
테스트 6 〉	통과 (85.09ms, 42.6MB)
테스트 7 〉	통과 (120.47ms, 53.4MB)
테스트 8 〉	통과 (113.82ms, 53.4MB)
테스트 9 〉	통과 (120.59ms, 53.4MB)
테스트 10 〉	통과 (115.42ms, 53.4MB)
테스트 11 〉	통과 (179.36ms, 53.5MB)
테스트 12 〉	통과 (169.74ms, 53.5MB)
테스트 13 〉	통과 (156.36ms, 53.5MB)
테스트 14 〉	통과 (169.24ms, 53.4MB)
테스트 15 〉	통과 (178.66ms, 53.4MB)
'''
def solution(a):
    
    if 2 >= len(a):
        return len(a)
    
    answer = 2
    left, right = a[0], a[-1]
    
    for i in range(1, len(a)-1):
        if left > a[i]:
            answer += 1
            left = a[i]
            
        if right > a[-i-1]:
            answer += 1
            right = a[-i-1]
    
    if left == right:
        return answer - 1
    else:
        return answer
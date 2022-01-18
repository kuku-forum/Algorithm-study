'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (9.81ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.03ms, 10.3MB)
테스트 9 〉	통과 (41.85ms, 10.5MB)
테스트 10 〉	통과 (74.48ms, 10.4MB)
테스트 11 〉	통과 (64.80ms, 10.4MB)
'''
def solution(s):
    answer = [0, 0]
    
    while int(s) != 1:
        
        std_len = len(s)
        s = s.replace('0', '')
        answer[1] += (std_len - len(s))
        
        s = bin(len(s))[2:]
        answer[0] += 1
        
    return answer
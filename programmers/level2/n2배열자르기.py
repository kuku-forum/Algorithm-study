
'''
정확성  테스트
테스트 1 〉	통과 (14.76ms, 17.3MB)
테스트 2 〉	통과 (18.85ms, 22.2MB)
테스트 3 〉	통과 (18.45ms, 22.5MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (26.66ms, 21.3MB)
테스트 7 〉	통과 (20.79ms, 22MB)
테스트 8 〉	통과 (20.52ms, 19.8MB)
테스트 9 〉	통과 (18.03ms, 21.7MB)
테스트 10 〉	통과 (17.82ms, 21.7MB)
테스트 11 〉	통과 (30.50ms, 21.6MB)
테스트 12 〉	통과 (18.30ms, 20.5MB)
테스트 13 〉	통과 (19.23ms, 21.6MB)
테스트 14 〉	통과 (18.20ms, 21.4MB)
테스트 15 〉	통과 (19.06ms, 21.1MB)
테스트 16 〉	통과 (19.06ms, 21.4MB)
테스트 17 〉	통과 (19.50ms, 21.3MB)
테스트 18 〉	통과 (24.27ms, 22.3MB)
테스트 19 〉	통과 (20.89ms, 21.4MB)
테스트 20 〉	통과 (16.59ms, 20.7MB)
'''
def solution(n, left, right):
    answer = []
    
    for idx in range(left, right+1):
        q, r = divmod(idx, n)
        
        if q >= r:
            answer.append(q + 1)
        else:
            answer.append(r + 1)
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.3MB)
테스트 3 〉	통과 (0.00ms, 10.3MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.3MB)
테스트 6 〉	통과 (0.00ms, 10.3MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.3MB)
테스트 10 〉	통과 (0.00ms, 10.3MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.00ms, 10.3MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.00ms, 10.3MB)
테스트 16 〉	통과 (0.01ms, 10.3MB)
테스트 17 〉	통과 (0.01ms, 10.3MB)
테스트 18 〉	통과 (0.01ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.3MB)
테스트 20 〉	통과 (0.01ms, 10.3MB)
테스트 21 〉	통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (3.56ms, 10.5MB)
테스트 2 〉	통과 (3.72ms, 10.6MB)
테스트 3 〉	통과 (3.82ms, 10.4MB)
테스트 4 〉	통과 (3.83ms, 10.6MB)
'''
def calc(answer, space, width):
    q, r = divmod(space, width)
    if r == 0:
        answer += q
    else:
        answer += q + 1
    
    return answer

def solution(n, stations, w):
    answer = 0
    start = 0
    width = 2*w + 1
    
    for loc in stations:
        left = loc-w
        
        if 1 > left:
            start = loc+w
            continue
            
        space = left - start - 1
        answer = calc(answer, space, width)
        start = loc+w
        if start >= n:
            break
    else:
        space = n - start 
        answer = calc(answer, space, width)
    
    return answer
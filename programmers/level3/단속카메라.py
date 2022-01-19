'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (0.56ms, 10.6MB)
테스트 2 〉	통과 (0.43ms, 10.2MB)
테스트 3 〉	통과 (0.84ms, 10.5MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (1.01ms, 10.6MB)
'''
def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    pos = routes[0][1]
    
    for start, end in routes[1:]:
        if start > pos:
            pos = end
            answer += 1
        
    return answer

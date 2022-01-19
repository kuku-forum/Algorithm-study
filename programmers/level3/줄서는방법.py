'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.02ms, 10MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
'''
def solution(n, k):
    
    answer = []
    
    people = [i for i in range(1, n+1)]
    factorial = []
    tmp = 1
    for i in range(1, n):
        tmp *= i
        factorial.append(tmp)
    factorial = factorial[::-1]
    
    for denom in factorial:
        q = (k - 1) // denom
        idx = q % len(people)
        
        # idx를 통해 people 값을 못 가져 오는것으로 보임
        answer.append(people.pop(idx))
        
    answer.extend(people)
    
    return answer
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.45ms, 10.1MB)
테스트 3 〉	통과 (0.19ms, 10.1MB)
테스트 4 〉	통과 (0.09ms, 9.97MB)
테스트 5 〉	통과 (246.92ms, 14.8MB)
테스트 6 〉	통과 (30.29ms, 11.8MB)
테스트 7 〉	통과 (2.13ms, 10.2MB)
테스트 8 〉	통과 (0.62ms, 10.2MB)
테스트 9 〉	통과 (1.03ms, 10.2MB)
테스트 10 〉	통과 (20.11ms, 14.6MB)
테스트 11 〉	통과 (1.89ms, 9.99MB)
'''
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    case_id = list(permutations(user_id, len(banned_id)))
    
    for case in case_id:
        for name, banned in zip(case, banned_id):
            break_trigger = False
            if len(name) != len(banned):
                break
            
            for n, b in zip(name, banned):
                if b == '*':
                    continue
                if n != b:
                    break_trigger = True
                    break
            if break_trigger:
                break
        else:
            case = set(case)
            if case not in answer:
                answer.append(case)
            
    return len(answer)
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.10ms, 10.3MB)
테스트 5 〉	통과 (0.33ms, 10.2MB)
테스트 6 〉	통과 (2.42ms, 10.1MB)
테스트 7 〉	통과 (20.45ms, 10.2MB)
테스트 8 〉	통과 (26.32ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.3MB)
테스트 10 〉	통과 (2.02ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.2MB)
테스트 12 〉	통과 (13.24ms, 10.2MB)
테스트 13 〉	통과 (9.68ms, 10.2MB)
테스트 14 〉	통과 (8.64ms, 10.2MB)
테스트 15 〉	통과 (8.71ms, 10.2MB)
테스트 16 〉	통과 (1.07ms, 10.2MB)
테스트 17 〉	통과 (8.65ms, 10.2MB)
'''
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for dungeon in permutations(dungeons):
        tmp = k
        cnt = 0
        
        for start, end in dungeon:
            if tmp >= start:
                tmp -= end
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt
    
    return answer
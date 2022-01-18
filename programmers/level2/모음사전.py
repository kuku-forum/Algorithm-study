'''
정확성  테스트
테스트 1 〉	통과 (0.82ms, 10.4MB)
테스트 2 〉	통과 (0.82ms, 10.4MB)
테스트 3 〉	통과 (1.70ms, 10.4MB)
테스트 4 〉	통과 (1.09ms, 10.5MB)
테스트 5 〉	통과 (0.96ms, 10.4MB)
테스트 6 〉	통과 (0.88ms, 10.5MB)
테스트 7 〉	통과 (1.73ms, 10.4MB)
테스트 8 〉	통과 (0.90ms, 10.4MB)
테스트 9 〉	통과 (1.62ms, 10.4MB)
테스트 10 〉	통과 (1.30ms, 10.4MB)
테스트 11 〉	통과 (1.69ms, 10.3MB)
테스트 12 〉	통과 (0.89ms, 10.3MB)
테스트 13 〉	통과 (1.84ms, 10.4MB)
테스트 14 〉	통과 (1.70ms, 10.5MB)
테스트 15 〉	통과 (0.93ms, 10.3MB)
테스트 16 〉	통과 (0.93ms, 10.4MB)
테스트 17 〉	통과 (0.97ms, 10.4MB)
테스트 18 〉	통과 (0.88ms, 10.4MB)
테스트 19 〉	통과 (0.99ms, 10.5MB)
테스트 20 〉	통과 (0.86ms, 10.4MB)
테스트 21 〉	통과 (1.39ms, 10.4MB)
테스트 22 〉	통과 (0.85ms, 10.5MB)
테스트 23 〉	통과 (0.82ms, 10.4MB)
테스트 24 〉	통과 (1.17ms, 10.4MB)
테스트 25 〉	통과 (1.57ms, 10.3MB)
테스트 26 〉	통과 (0.85ms, 10.4MB)
테스트 27 〉	통과 (0.96ms, 10.4MB)
테스트 28 〉	통과 (0.98ms, 10.4MB)
테스트 29 〉	통과 (0.83ms, 10.4MB)
테스트 30 〉	통과 (1.12ms, 10.4MB)
테스트 31 〉	통과 (1.74ms, 10.5MB)
테스트 32 〉	통과 (1.37ms, 10.5MB)
테스트 33 〉	통과 (2.01ms, 10.4MB)
테스트 34 〉	통과 (1.12ms, 10.5MB)
테스트 35 〉	통과 (0.99ms, 10.3MB)
테스트 36 〉	통과 (0.99ms, 10.4MB)
테스트 37 〉	통과 (1.11ms, 10.4MB)
테스트 38 〉	통과 (1.60ms, 10.4MB)
테스트 39 〉	통과 (0.96ms, 10.4MB)
테스트 40 〉	통과 (0.87ms, 10.3MB)
'''
from itertools import product

def solution(target):
    answer = 0
    alpha = 'AEIOU'
    word_lst = []
    
    for i in range(1, 6):
        word_lst += list(map(lambda x: ''.join(x), product(alpha, repeat=i)))
        
    word_lst.sort()
    
    for i, word in enumerate(word_lst):
        if word == target:
            return i+1
    
    return answer
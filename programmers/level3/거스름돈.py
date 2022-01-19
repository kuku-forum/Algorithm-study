'''
정확성  테스트
테스트 1 〉	통과 (3.78ms, 10.3MB)
테스트 2 〉	통과 (2.21ms, 10.3MB)
테스트 3 〉	통과 (1.41ms, 10.2MB)
테스트 4 〉	통과 (1.90ms, 10.3MB)
테스트 5 〉	통과 (1.47ms, 10.2MB)
테스트 6 〉	통과 (1.29ms, 10.3MB)
테스트 7 〉	통과 (3.19ms, 10.2MB)
테스트 8 〉	통과 (3.64ms, 10.3MB)
테스트 9 〉	통과 (3.35ms, 10.3MB)
테스트 10 〉	통과 (1.73ms, 10.2MB)
테스트 11 〉	통과 (2.99ms, 10.4MB)
테스트 12 〉	통과 (2.33ms, 10.2MB)
테스트 13 〉	통과 (0.84ms, 10.3MB)
테스트 14 〉	통과 (3.62ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (251.72ms, 10.8MB)
테스트 2 〉	통과 (309.95ms, 11.9MB)
테스트 3 〉	통과 (243.68ms, 11.3MB)
테스트 4 〉	통과 (252.32ms, 10.8MB)
테스트 5 〉	통과 (447.09ms, 13.1MB)
테스트 6 〉	통과 (349.82ms, 12.1MB)
'''
def solution(n, money):
    rest = [1] + [0]*n
    
    for coin in money:
        for i in range(coin, n+1):
            # print(i, coin, i-coin)
            rest[i] += rest[i-coin]
        # print(rest)
        # print()
        
    return rest[n]
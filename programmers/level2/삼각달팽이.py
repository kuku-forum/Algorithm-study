
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (1.35ms, 10.8MB)
테스트 5 〉	통과 (1.27ms, 10.6MB)
테스트 6 〉	통과 (1.40ms, 10.9MB)
테스트 7 〉	통과 (1393.93ms, 58.6MB)
테스트 8 〉	통과 (1098.09ms, 58.7MB)
테스트 9 〉	통과 (1268.73ms, 56.9MB)
'''
def solution(n):
    answer = [[0 for _ in range(1, i + 1)] for i in range(1, n + 1)]
    
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            answer[x][y] = num
            num += 1
            
    return sum(answer, [])

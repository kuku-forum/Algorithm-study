
'''
정확성  테스트
테스트 1 〉	통과 (0.70ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (16.14ms, 11.3MB)
테스트 5 〉	통과 (10.65ms, 11.2MB)
테스트 6 〉	통과 (0.15ms, 10.4MB)
테스트 7 〉	통과 (0.16ms, 10.5MB)
테스트 8 〉	통과 (15.36ms, 11.3MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
'''
def solution(N, number):
    answer = -1
    
    dp = []
    
    for i in range(1, 9):
        numbers = set()
        numbers.add(int(str(N) * i))
        
        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)
        
        if number in numbers:
            answer = i
            break
        
        dp.append(numbers)
    
    return answer
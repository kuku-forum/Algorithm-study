'''
정확성  테스트
테스트 1 〉	통과 (0.87ms, 10.1MB)
테스트 2 〉	통과 (66.10ms, 26.2MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.49ms, 10.3MB)
테스트 5 〉	통과 (0.61ms, 10.3MB)
테스트 6 〉	통과 (0.54ms, 10.3MB)
테스트 7 〉	통과 (95.90ms, 26MB)
테스트 8 〉	통과 (89.16ms, 25.3MB)
테스트 9 〉	통과 (96.70ms, 25MB)
테스트 10 〉	통과 (202.59ms, 26.7MB)
테스트 11 〉	통과 (200.11ms, 26.8MB)
'''
def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
            continue
        else:
            num = list('0' + bin(num)[2:])
            idx = ''.join(num).rfind('0')
            num[idx] = '1'
            num[idx + 1] = '0'
            answer.append(int(''.join(num), 2))
    
    return answer
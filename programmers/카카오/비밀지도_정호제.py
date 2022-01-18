'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
'''
def solution(n, arr1, arr2):
    answer = []
    
    for tmp1, tmp2 in zip(arr1, arr2):
        row = bin(tmp1 | tmp2)[2:]
        if n > len(row):
            row = '0' * (n - len(row)) + row
        answer.append(row.replace('0', ' ').replace('1', '#'))
        
    return answer
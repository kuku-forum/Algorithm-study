
'''
정확성  테스트
테스트 1 〉	통과 (2.14ms, 10.4MB)
테스트 2 〉	통과 (38.68ms, 10.9MB)
테스트 3 〉	통과 (42.33ms, 11.4MB)
테스트 4 〉	통과 (0.93ms, 10.3MB)
테스트 5 〉	통과 (30.00ms, 10.9MB)
테스트 6 〉	통과 (17.06ms, 11MB)
테스트 7 〉	통과 (0.96ms, 10.2MB)
테스트 8 〉	통과 (0.49ms, 10.1MB)
테스트 9 〉	통과 (0.41ms, 10.1MB)
테스트 10 〉	통과 (28.01ms, 10.7MB)
테스트 11 〉	통과 (3.21ms, 10.1MB)
테스트 12 〉	통과 (0.83ms, 10.3MB)
테스트 13 〉	통과 (33.33ms, 10.8MB)
테스트 14 〉	통과 (42.13ms, 11.2MB)
테스트 15 〉	통과 (13.28ms, 10.6MB)
테스트 16 〉	통과 (9.63ms, 10.7MB)
'''
def solution(arr1, arr2):
    answer = []
    
    for tmp1 in arr1:
        tmp = []
        for tmp2 in list(map(list,zip(*arr2))):
            tmp.append(sum(a*b for a, b in zip(tmp1, tmp2)))
        answer.append(tmp)
    
    return answer

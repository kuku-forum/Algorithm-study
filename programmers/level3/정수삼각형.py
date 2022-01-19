
'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.05ms, 10.2MB)
테스트 4 〉	통과 (0.17ms, 10.1MB)
테스트 5 〉	통과 (1.33ms, 10.3MB)
테스트 6 〉	통과 (0.36ms, 10.2MB)
테스트 7 〉	통과 (2.24ms, 10.3MB)
테스트 8 〉	통과 (0.29ms, 10.2MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.17ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (81.39ms, 14.2MB)
테스트 2 〉	통과 (35.05ms, 13.2MB)
테스트 3 〉	통과 (49.75ms, 14.6MB)
테스트 4 〉	통과 (45.91ms, 14.1MB)
테스트 5 〉	통과 (42.93ms, 14MB)
테스트 6 〉	통과 (53.25ms, 14.7MB)
테스트 7 〉	통과 (46.57ms, 14.4MB)
테스트 8 〉	통과 (38.57ms, 13.6MB)
테스트 9 〉	통과 (43.19ms, 13.9MB)
테스트 10 〉	통과 (86.14ms, 14.5MB)
'''
def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])

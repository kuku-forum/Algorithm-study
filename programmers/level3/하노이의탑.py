'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (0.11ms, 10.4MB)
테스트 6 〉	통과 (0.23ms, 10.3MB)
테스트 7 〉	통과 (0.52ms, 10.5MB)
테스트 8 〉	통과 (1.01ms, 10.6MB)
테스트 9 〉	통과 (1.91ms, 10.9MB)
테스트 10 〉	통과 (4.09ms, 11.6MB)
테스트 11 〉	통과 (7.64ms, 12.9MB)
테스트 12 〉	통과 (15.49ms, 15.7MB)
테스트 13 〉	통과 (30.82ms, 18.7MB)
'''
answer = []
def hanoi(n, start, aux, end):

    if n == 1:
        print('#1', n)
        answer.append([start, end])
        return
    
    hanoi(n-1, start, end, aux)
    print('#2', n)
    answer.append([start, end])
    
    hanoi(n-1, aux, start, end)
    print('#3', n)
    return

def solution(n):
    hanoi(n, 1, 2, 3)
    return answer

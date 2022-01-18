#%%

def solution(numbers):
    return str(int(''.join(sorted(map(str, numbers), key = lambda x : x*3, reverse = True))))

#%%
'''
정확성  테스트
테스트 1 〉	통과 (745.16ms, 23.3MB)
테스트 2 〉	통과 (244.17ms, 17.1MB)
테스트 3 〉	통과 (1268.50ms, 27.4MB)
테스트 4 〉	통과 (1.58ms, 10.5MB)
테스트 5 〉	통과 (590.03ms, 21.9MB)
테스트 6 〉	통과 (480.74ms, 20.4MB)
테스트 7 〉	통과 (0.03ms, 10.4MB)
테스트 8 〉	통과 (0.03ms, 10.5MB)
테스트 9 〉	통과 (0.02ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.3MB)
테스트 12 〉	통과 (0.02ms, 10.3MB)
테스트 13 〉	통과 (0.02ms, 10.3MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
테스트 15 〉	통과 (0.02ms, 10.3MB)
'''
def solution(numbers):
    return str(int(''.join(sorted(map(str, numbers), key = lambda x: x*3, reverse = True))))
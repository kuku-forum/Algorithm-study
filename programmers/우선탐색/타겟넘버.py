def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(val, i):
        global answer
        
        if val == target and i == len(numbers):
            answer += 1
            return
            
        if i == len(numbers):
            return
        
        dfs(val - numbers[i], i + 1)
        dfs(val + numbers[i], i + 1)
        return 
    
    dfs(0, 0)
            
    return answer


#%%
'''
정확성  테스트
테스트 1 〉	통과 (306.88ms, 10.2MB)
테스트 2 〉	통과 (307.15ms, 10.2MB)
테스트 3 〉	통과 (0.65ms, 10.2MB)
테스트 4 〉	통과 (1.21ms, 10.2MB)
테스트 5 〉	통과 (9.66ms, 10.2MB)
테스트 6 〉	통과 (0.67ms, 10.2MB)
테스트 7 〉	통과 (0.32ms, 10.2MB)
테스트 8 〉	통과 (2.58ms, 10.2MB)
'''
def dfs(sum_num, numbers, idx, target):
    global answer
    
    if idx == len(numbers):
        if target == sum_num:
            answer += 1
            return 
        return
    
    dfs(sum_num + numbers[idx], numbers, idx+1, target)
    dfs(sum_num - numbers[idx], numbers, idx+1, target)

def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, numbers, 0, target)
    
    return answer
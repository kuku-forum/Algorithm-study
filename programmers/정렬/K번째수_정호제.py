def solution(array, commands):
    
    answer = []
    
    for command in commands:
        
        tmp_arr = sorted(array[command[0]-1 : command[1]])
        answer.append(tmp_arr[command[2]-1])
    
    return answer

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
'''
def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        answer.append(sorted(array[i-1: j])[k-1])
        
    return answer
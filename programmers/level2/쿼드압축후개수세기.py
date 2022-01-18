'''
정확성  테스트
테스트 1 〉	통과 (0.62ms, 10.1MB)
테스트 2 〉	통과 (0.53ms, 10MB)
테스트 3 〉	통과 (0.37ms, 10.1MB)
테스트 4 〉	통과 (0.06ms, 10.2MB)
테스트 5 〉	통과 (235.98ms, 12MB)
테스트 6 〉	통과 (84.64ms, 12MB)
테스트 7 〉	통과 (42.54ms, 12.1MB)
테스트 8 〉	통과 (26.13ms, 12MB)
테스트 9 〉	통과 (36.18ms, 12.3MB)
테스트 10 〉	통과 (90.22ms, 18.8MB)
테스트 11 〉	통과 (0.06ms, 10.1MB)
테스트 12 〉	통과 (0.06ms, 10.3MB)
테스트 13 〉	통과 (40.87ms, 12.1MB)
테스트 14 〉	통과 (188.50ms, 18.6MB)
테스트 15 〉	통과 (220.46ms, 18.8MB)
테스트 16 〉	통과 (68.18ms, 12.1MB)
'''
def quard_tree(x_start, x_end, y_start, y_end, answer, arr):
    
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            std = arr[y_start][x_start]
            
            if arr[y][x] != std:
                answer = quard_tree(x_start , (x_start + x_end)//2, y_start , (y_start + y_end)//2, answer, arr)
                answer = quard_tree(x_start , (x_start + x_end)//2, (y_start + y_end)//2, y_end, answer, arr)
                answer = quard_tree((x_start + x_end)//2, x_end, y_start , (y_start + y_end)//2, answer, arr)
                answer = quard_tree((x_start + x_end)//2, x_end, (y_start + y_end)//2, y_end, answer, arr)
                return answer
    
    if std == 0: answer[0] += 1
    else: answer[1] += 1
    
    return answer
    

def solution(arr):
    answer = [0, 0]
    answer = quard_tree(0, len(arr), 0, len(arr), answer, arr)
        
    return answer
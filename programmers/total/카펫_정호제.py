def chk_sum(brown, yellow, y, x):
    num = brown + yellow
    
    while True:
        num -= 2*(x + y - 2)
        if yellow == num: return True
        
        x -= 2
        y -= 2
        
        if yellow > num  or 1 > x or 1 > y: return False
        
def solution(brown, yellow):
    answer = [0, 0]
    num = brown + yellow
    
    for y_len in range(1, int(num**0.5) + 1):
        
        if num%y_len != 0:
            continue
        
        x_len = num//y_len
        trig = chk_sum(brown, yellow, y_len, x_len)
        
        if trig:
            answer[0] = x_len
            answer[1] = y_len
    
    return answer

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.19ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.07ms, 10.3MB)
테스트 7 〉	통과 (0.16ms, 10.3MB)
테스트 8 〉	통과 (0.21ms, 10.2MB)
테스트 9 〉	통과 (0.18ms, 10.2MB)
테스트 10 〉	통과 (0.23ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
'''
def solution(brown, yellow):
    
    for h in range(3, brown//2):
        w = (brown - h*2)/2 + 2
        
        if yellow == (w-2)*(h-2):
            return [int(w), int(h)]
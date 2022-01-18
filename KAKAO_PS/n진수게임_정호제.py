'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.1MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.13ms, 10.2MB)
테스트 6 〉	통과 (0.13ms, 10.1MB)
테스트 7 〉	통과 (0.12ms, 10.1MB)
테스트 8 〉	통과 (0.15ms, 10.2MB)
테스트 9 〉	통과 (0.15ms, 10.1MB)
테스트 10 〉	통과 (0.15ms, 10.1MB)
테스트 11 〉	통과 (0.18ms, 10.2MB)
테스트 12 〉	통과 (0.16ms, 10.2MB)
테스트 13 〉	통과 (0.17ms, 10.1MB)
테스트 14 〉	통과 (29.56ms, 10.3MB)
테스트 15 〉	통과 (26.88ms, 10.1MB)
테스트 16 〉	통과 (27.17ms, 10.2MB)
테스트 17 〉	통과 (1.03ms, 10.1MB)
테스트 18 〉	통과 (1.50ms, 10.1MB)
테스트 19 〉	통과 (0.39ms, 10.1MB)
테스트 20 〉	통과 (1.15ms, 10.1MB)
테스트 21 〉	통과 (7.13ms, 10.1MB)
테스트 22 〉	통과 (2.77ms, 10.1MB)
테스트 23 〉	통과 (10.21ms, 10.2MB)
테스트 24 〉	통과 (12.17ms, 10.1MB)
테스트 25 〉	통과 (10.39ms, 10.2MB)
테스트 26 〉	통과 (4.28ms, 10.2MB)
'''
def change_num(num, n, dic):
    rev_base = ''

    while num > 0:
        num, r = divmod(num, n)
        rev_base += dic[r].upper()
        
    return rev_base[::-1].lstrip('0')

def solution(n, t, m, p):
    answer = ''
    nums, num = '0', 1
    alpha_dic = {i: hex(i)[2:].upper() for i in range(16)}
    
    while t*m + 1 > len(nums):
        nums += change_num(num, n, alpha_dic)
        num += 1
        
    for i in range(p, t*m + 1, m):
        answer += nums[i - 1]
    
    return answer



'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.89ms, 10.2MB)
테스트 6 〉	통과 (0.91ms, 10.4MB)
테스트 7 〉	통과 (0.89ms, 10.3MB)
테스트 8 〉	통과 (0.33ms, 10.3MB)
테스트 9 〉	통과 (0.35ms, 10.3MB)
테스트 10 〉	통과 (0.57ms, 10.3MB)
테스트 11 〉	통과 (0.47ms, 10.2MB)
테스트 12 〉	통과 (0.27ms, 10.3MB)
테스트 13 〉	통과 (0.26ms, 10.3MB)
테스트 14 〉	통과 (105.16ms, 10.5MB)
테스트 15 〉	통과 (108.68ms, 10.5MB)
테스트 16 〉	통과 (107.67ms, 10.5MB)
테스트 17 〉	통과 (7.82ms, 10.2MB)
테스트 18 〉	통과 (3.64ms, 10.3MB)
테스트 19 〉	통과 (1.41ms, 10.3MB)
테스트 20 〉	통과 (2.94ms, 10.3MB)
테스트 21 〉	통과 (24.12ms, 10.3MB)
테스트 22 〉	통과 (17.36ms, 10.3MB)
테스트 23 〉	통과 (34.50ms, 10.4MB)
테스트 24 〉	통과 (136.67ms, 10.5MB)
테스트 25 〉	통과 (185.58ms, 10.8MB)
테스트 26 〉	통과 (22.25ms, 10.3MB)
'''
def solution(n, t, m, p):
    alp_dic = {num: chr(alp) for num, alp in zip(range(10, 16), range(ord('A'), ord('G')))}
    process_total = ''
    
    for num in range(t*m):
        process = ''
        while True:
            num, r = divmod(num, n)
            if r >= 10:
                process = alp_dic[r] + process
            else:
                process = str(r) + process
            if num == 0:
                break    
        process_total += process
            
    process_my = ''
    for i in range(p-1, t*m, m):
        process_my += process_total[i]
        
    return process_my
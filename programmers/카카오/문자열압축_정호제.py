'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.3MB)
테스트 2 〉	통과 (0.40ms, 10.3MB)
테스트 3 〉	통과 (0.21ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.46ms, 10.3MB)
테스트 8 〉	통과 (0.46ms, 10.2MB)
테스트 9 〉	통과 (0.75ms, 10.3MB)
테스트 10 〉	통과 (2.67ms, 10.4MB)
테스트 11 〉	통과 (0.10ms, 10.3MB)
테스트 12 〉	통과 (0.11ms, 10.2MB)
테스트 13 〉	통과 (0.12ms, 10.3MB)
테스트 14 〉	통과 (0.67ms, 10.3MB)
테스트 15 〉	통과 (0.12ms, 10.4MB)
테스트 16 〉	통과 (0.02ms, 10.2MB)
테스트 17 〉	통과 (1.25ms, 10.3MB)
테스트 18 〉	통과 (1.23ms, 10.3MB)
테스트 19 〉	통과 (1.24ms, 10.3MB)
테스트 20 〉	통과 (3.18ms, 10.2MB)
테스트 21 〉	통과 (2.91ms, 10.2MB)
테스트 22 〉	통과 (2.93ms, 10.3MB)
테스트 23 〉	통과 (2.96ms, 10.3MB)
테스트 24 〉	통과 (2.68ms, 10.3MB)
테스트 25 〉	통과 (2.97ms, 10.3MB)
테스트 26 〉	통과 (2.94ms, 10.2MB)
테스트 27 〉	통과 (2.87ms, 10.3MB)
테스트 28 〉	통과 (0.02ms, 10.3MB)
'''
def combine_str(num, total_str, init_str):
    if num == 1:
            total_str += init_str
    else:
        total_str += str(num) + init_str
        
    return total_str

def solution(s):
    min_len = len(s)
    
    for term in range(1, len(s)+1):
        init_tmp = ''
        total_tmp = ''
        cnt = 1
        for start in range(0, len(s), term):
            tmp = s[start:start+term]
            
            if not init_tmp:
                init_tmp = tmp
            elif init_tmp == tmp:
                cnt += 1
            else:
                total_tmp = combine_str(cnt, total_tmp, init_tmp)
                init_tmp = tmp
                cnt = 1
        else:
            total_tmp = combine_str(cnt, total_tmp, init_tmp)
            
        min_len = min(min_len, len(total_tmp))
    return min_len
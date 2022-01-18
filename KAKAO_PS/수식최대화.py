'''
정확성  테스트
테스트 1 〉	통과 (0.23ms, 10.5MB)
테스트 2 〉	통과 (0.25ms, 10.5MB)
테스트 3 〉	통과 (0.38ms, 10.5MB)
테스트 4 〉	통과 (0.44ms, 10.5MB)
테스트 5 〉	통과 (0.55ms, 10.5MB)
테스트 6 〉	통과 (0.50ms, 10.5MB)
테스트 7 〉	통과 (0.51ms, 10.5MB)
테스트 8 〉	통과 (0.53ms, 10.5MB)
테스트 9 〉	통과 (0.66ms, 10.5MB)
테스트 10 〉	통과 (0.75ms, 10.5MB)
테스트 11 〉	통과 (0.68ms, 10.5MB)
테스트 12 〉	통과 (0.74ms, 10.5MB)
테스트 13 〉	통과 (0.88ms, 10.5MB)
테스트 14 〉	통과 (1.00ms, 10.5MB)
테스트 15 〉	통과 (1.05ms, 10.5MB)
테스트 16 〉	통과 (0.23ms, 10.5MB)
테스트 17 〉	통과 (0.30ms, 10.5MB)
테스트 18 〉	통과 (0.29ms, 10.5MB)
테스트 19 〉	통과 (0.28ms, 10.5MB)
테스트 20 〉	통과 (0.30ms, 10.5MB)
테스트 21 〉	통과 (0.90ms, 10.5MB)
테스트 22 〉	통과 (1.40ms, 10.5MB)
테스트 23 〉	통과 (0.22ms, 10.5MB)
테스트 24 〉	통과 (1.12ms, 10.5MB)
테스트 25 〉	통과 (0.96ms, 10.5MB)
테스트 26 〉	통과 (0.27ms, 10.5MB)
테스트 27 〉	통과 (1.08ms, 10.5MB)
테스트 28 〉	통과 (1.17ms, 10.5MB)
테스트 29 〉	통과 (0.87ms, 10.5MB)
테스트 30 〉	통과 (1.49ms, 10.5MB)
'''
import copy
from collections import deque

def solution(expression):
    
    opt_lst = [['+', '-', '*'], ['+', '*', '-'],
               ['-', '+', '*'], ['-', '*', '+'],
               ['*', '+', '-'], ['*', '-', '+']]
    exp_lst = deque([])
    num_lst = []
    tmp = ''
    
    for i in expression:
        if i.isdigit():
            tmp += i
        else:
            exp_lst.append(tmp)
            exp_lst.append(i)
            tmp = ''
    exp_lst.append(tmp)
    
    for opts in opt_lst:
        tmp1_lst = copy.deepcopy(exp_lst)
        
        for opt in opts:
            tmp2_lst = deque([])
            
            while tmp1_lst:
                factor = tmp1_lst.popleft()
                
                if factor == opt:
                    num1 = tmp2_lst.pop()
                    num2 = tmp1_lst.popleft()
                    tmp2_lst.append(str(eval(num1 + factor + num2)))
                else:
                    tmp2_lst.append(factor)
            
            if len(tmp2_lst) != 1:
                tmp1_lst = tmp2_lst
            else:
                break
        
        if  tmp2_lst:
            num_lst.append(abs(int(tmp2_lst[0])))
    
    return max(num_lst)
from itertools import permutations

def solution(numbers):
    str_lst, num_lst = [], set([])
    for i in range(1, len(numbers) + 1):
        str_lst.extend(list(permutations(numbers, i)))
    
    for num in str_lst:
        tmp = ''
        for n in num:
            tmp += n
        num_lst.add(int(tmp))
    
    cnt = 0    
    for num in num_lst:
        prim_trg = True
        
        if 2 > num:
            continue
            
        if 3 >= num >= 2:
            max_i = 2 # 2,3 -> 2
        else:
            max_i = int(num**0.5) + 1

        for i in range(2, max_i):
            if num % i == 0:
                prim_trg = False
                break
                
        if prim_trg:
            cnt += 1
                        
    return cnt

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.4MB)
테스트 2 〉	통과 (2.05ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (1.84ms, 10.5MB)
테스트 5 〉	통과 (9.91ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.09ms, 10.4MB)
테스트 8 〉	통과 (11.13ms, 10.5MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (5.54ms, 10.4MB)
테스트 11 〉	통과 (0.55ms, 10.4MB)
테스트 12 〉	통과 (0.28ms, 10.4MB)
'''
from itertools import permutations

def solution(numbers):
    answer = set()
    
    for i in range(1, len(numbers) + 1):
        for num in permutations(numbers, i):
            num = int(''.join(num))
            
            if 1 >= num:
                continue
            elif num == 2 or num == 3:
                answer.add(num)
                continue
                
            for j in range(2, int(num**0.5)+1):
                if num % j == 0:
                    break
            else:
                answer.add(num)

    return len(answer)
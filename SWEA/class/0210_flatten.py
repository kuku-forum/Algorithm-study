
from my_package.hjtc import swea_tc as print
def min_func(arr):
    min_val = int(1e8)
    idx = -1
    
    for i, num in enumerate(arr):
        if min_val > num:
            min_val = num
            idx = i
            
    return idx, min_val


def max_func(arr):
    max_val = int(-1e8)
    idx = -1
    
    for i, num in enumerate(arr):
        if num > max_val:
            max_val = num
            idx = i
            
    return idx, max_val

for t in range(1, 11):
    
    answer = 0
    N = int(input())
    
    num_list = list(map(int, input().split()))
        
        
    for _ in range(N):
        max_idx, max_num = max_func(num_list)
        min_idx, min_num = min_func(num_list)
        
        num_list[max_idx] -= 1
        num_list[min_idx] += 1
    
    _, max_num = max_func(num_list)
    _, min_num = min_func(num_list)
    answer = max_num - min_num
    
    print(f'#{t} {answer}')   

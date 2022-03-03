
T = int(input())

def min_func(arr):
    min_val = int(1e8)
    
    for num in arr:
        if min_val > num:
            min_val = num
            
    return min_val


def max_func(arr):
    max_val = int(-1e8)
    
    for num in arr:
        if num > max_val:
            max_val = num
            
    return max_val
    
    
for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    num_list = list(map(int, input().split()))
    sum_list = []
    
    for i in range(N - M + 1):
        sum_val = 0
        for j in range(i, i + M):
            sum_val += num_list[j]
            
        sum_list.append(sum_val)
    
    answer = max_func(sum_list) - min_func(sum_list)
    
    print(f'#{t} {answer}')
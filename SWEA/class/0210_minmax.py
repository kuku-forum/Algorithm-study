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
    _ = input()
    
    num_list = list(map(int, input().split()))
    answer = max_func(num_list) - min_func(num_list)
    
    print(f'#{t} {answer}')
def sum_func(arr):
    result = 0
    for num in arr:
        result += num
        
    return result

def subset(num_list, K):
    result = 0
    
    for i in range(1 << len(num_list)):
        tmp = []
        for j in range(len(num_list)):
            
            if i & (1<<j):
                tmp.append(num_list[j])
                
        if sum_func(tmp) == K:
            result += 1
    return result


for t in range(1, int(input()) + 1):
    _, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{t} {subset(arr, K)}')
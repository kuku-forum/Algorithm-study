def combi_gen(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        element = arr[i]
        
        for c in combi_gen(arr[i + 1:], n - 1):
            result.append([element] + c)
    
    return result


def sum_func(arr):
    result = 0
    
    for num in arr:
        result += num
        
    return result


def solve(num_list):
    
    for i in range(1, len(num_list) + 1):
        for subset in combi_gen(num_list, i):
            if sum_func(subset) == 0:
                return 1
    return 0

    
T = int(input())
    
for t in range(1, T + 1):    
    print(f'#{t} {solve(list(map(int, input().split())))}')
def combi_gen(arr, n):
    result = []
    
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        element = arr[i]
        
        for c in combi_gen(arr[i + 1:], n - 1):
            result.append([element] + c)
            
    return result



num_list = [1, 2, 3]

for i in range(1 << len(num_list)):
    print('*'*20)
    print(f'i:{i}: {bin(i)[2:].zfill(len(num_list))}')
    
    for j in range(len(num_list)):
        # print(f'j:{j} -> 1<<j(2^j): {bin(1<<j)[2:].zfill(len(num_list))}')
        
        if i & (1<<j):
            print('True')
            print(f'i:{i} -> {bin(i)[2:].zfill(len(num_list))}')
            print(f'j:{j} -> {bin(1<<j)[2:].zfill(len(num_list))}')
            # print()
    print()
    
    

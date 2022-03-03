for t in range(1, int(input()) + 1):
    
    N = int(input())
    num_list = list(map(int, input().split()))
    
    for i in range(N):
        if i%2 == 0:
            flag = 'max'
        else:
            flag = 'min'
        special_idx = i
        
        for j in range(i + 1, N):
            if flag == 'min' and num_list[special_idx] > num_list[j]:
                special_idx = j
                
            if flag == 'max' and num_list[j] > num_list[special_idx]:
                special_idx = j
        
        num_list[i], num_list[special_idx] = num_list[special_idx] , num_list[i]
        
    
    print(f'#{t} {" ".join(map(str, num_list[:10]))}')
for t in range(1, int(input()) + 1):
    
    A, B = input().split()
    cnt = 0
    i = 0
    
    while len(A) - len(B) + 1 > i:
        flag = True
        for j, k in enumerate(range(i, i + len(B))):
            if A[k] != B[j]:
                flag = False
                break
                
        if flag:
            i = k
            cnt += 1
        i += 1
            
    min_cnt = len(A) - cnt*len(B) + cnt
    print(f'#{t} {min_cnt}')
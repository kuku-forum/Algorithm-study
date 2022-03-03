for t in range(1, int(input()) + 1):
    
    P, A, B = map(int, input().split())
    cnt_A = cnt_B = 0
    
    start = 1
    end = P
    
    while start <= end:
        mid = int((start + end)/2)
        cnt_A += 1
        
        if mid == A:
            break
        elif A > mid:
            start = mid
        else:
            end = mid
            
    start = 1
    end = P
    
    while start <= end:
        mid = int((start + end)/2)
        cnt_B += 1
        
        if mid == B:
            break
        elif B > mid:
            start = mid
        else:
            end = mid
    
    if cnt_A < cnt_B:
        answer = 'A'
    elif cnt_A > cnt_B:
        answer = 'B'
    else:
        answer = 0
        
    print(f'#{t} {answer}')
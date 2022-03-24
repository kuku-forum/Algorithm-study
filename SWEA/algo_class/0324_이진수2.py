for t in range(1, int(input()) + 1):
    num = float(input())
    answer = ''
    bound = 1
    
    while 13 > len(answer):
        q = 2**-bound
        
        if q > num:
            answer += '0'
        elif num > q:
            answer += '1'
            num -= q
        else:
            answer += '1'
            break    
        bound += 1
        
    else:
        answer = 'overflow'
    
    print(f'#{t}', answer)
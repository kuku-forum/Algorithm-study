for t in range(1, int(input()) + 1):
    case = list(input())
    chk_list = []
    
    while case:
        socket = case.pop(0)
        
        if not chk_list:
            chk_list.append(socket)
            continue
        
        if socket == chk_list[-1]:
            chk_list.append(socket)
        else:
            chk_list.pop()
            
    answer = 1
    
    if chk_list:
        answer = 0
        
    print(f'#{t} {answer}')
    
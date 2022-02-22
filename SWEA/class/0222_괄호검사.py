for t in range(1, int(input()) + 1):
    sentence = list(reversed(input()))
    
    socket_chk = []
    socket = ['(', ')', '{', '}']
    
    for _ in range(len(sentence)):
        unit = sentence.pop()
        
        if unit not in socket:
            continue
        
        if not socket_chk:
            socket_chk.append(unit)
            
        else:
            if socket_chk[-1] == '(' and unit == ')':
                socket_chk.pop()
            
            elif socket_chk[-1] == '{' and unit == '}':
                socket_chk.pop()
                
            else:
                socket_chk.append(unit)
                
                
    answer = 1
    if socket_chk:
        answer = 0
    
    print(f'#{t} {answer}')
    
    
    
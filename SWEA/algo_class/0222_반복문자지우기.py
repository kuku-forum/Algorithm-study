for t in range(1, int(input()) + 1):
    word = list(reversed(input()))
    
    while True:
        N = len(word)
        stack = []
        
        for _ in range(N):
            alp = word.pop()
            
            if not stack:
                stack.append(alp)
            elif stack[-1] == alp:
                stack.pop()
            else:
                stack.append(alp)
        
        word = stack    
        if N == len(word):
            break
    
    print(f'#{t} {len(word)}')
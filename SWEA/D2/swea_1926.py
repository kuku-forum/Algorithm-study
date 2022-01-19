N = int(input())
answer = []

for num in range(1, N+1):
    num = str(num)
    cnt = 0
    
    for n in num:        
        if n in ('3', '6', '9'):
            cnt += 1

    if cnt > 0:
        answer.append('-'*cnt)
    else:
        answer.append(num)

print(' '.join(answer))
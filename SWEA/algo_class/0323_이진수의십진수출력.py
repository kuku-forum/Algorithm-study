def bi2deci(num):
    result = 0
    for i in range(7):
        result += int(num[6-i])*pow(2,i)
    return result

for t in range(1, int(input()) + 1):
    info = list(input())
    answer = []
    
    for i in range(0, len(info), 7):
        answer.append(bi2deci(info[i:i+7]))
        
    print(f'#{t}', *answer)
    
T = int(input())

for t in range(1, T+1):
    print(f'#{t}')
    money = int(input())
    changes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = []
    
    for change in changes:
    
        if money//change == 0:
            answer.append(0)
        else:
            cnt, money = divmod(money, change)
            answer.append(cnt)
                
    print(' '.join(map(str, answer)))
T = int(input())

def solution(num):
    year = num[:4]
    month = num[4:6]
    day = num[6:]
    
    if int(month) in [1,3,5,7,8,10,12]:
        if 31 >= int(day) >= 1:
            return f'{year}/{month}/{day}'
    
    elif int(month) in [4, 6, 9, 11]:
        if 30 >= int(day) >= 1:
            return f'{year}/{month}/{day}'
    elif int(month) == 2:
        if 28 >= int(day) >= 1:
            return f'{year}/{month}/{day}'
    return -1
        
for i in range(1, T+1): 
    print(f'#{i} {solution(input())}')
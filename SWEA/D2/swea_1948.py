T = int(input())

day_dic = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def solution(SM, SD, EM, ED):
    
    SM, SD, EM, ED
    day1 = SD
    day2 = ED
    
    for M in range(1, SM):
        day1 += day_dic[M]
    
    for M in range(1, EM):
        day2 += day_dic[M]
    
    return day2 - day1 + 1

for t in range(1, T+1):
    SM, SD, EM, ED = map(int, input().split())
    answer = solution(SM, SD, EM, ED)
    print(f'#{t} {answer}')
'''
[1, 4, 99, 35, 50, 1000]
[2, 11, 20, 100, 200, 600]
'''

def solution(money, costs):
    money_list = [1, 5, 10, 50, 100, 500]
    total_money = 0
    
    idx = 5
    for idx in range(5, -1, -1):
        if costs[idx] > costs[idx-1]*5:
            cnt = money//money_list[idx-1]
            money %= money_list[idx-1]
            total_money += (cnt*costs[idx-1])
        else:
            cnt = money//money_list[idx]
            money %= money_list[idx]
            total_money += (cnt*costs[idx])
    
    total_money += money
        
    return total_money

solution(4578, [1, 4, 99, 35, 50, 1000]) # 2308
solution(1999, [2, 11, 20, 100, 200, 600]) # 2798


'''
def solution(money, costs):
    answer = 0
    hwapea = [1, 5, 10, 50, 100, 500]
    i = 5
    while i:
        if costs[i] > costs[i - 1] * 5:
            res, money = divmod(money, hwapea[i - 1])
            answer += res * costs[i - 1]
        else:
            res, money = divmod(money, hwapea[i])
            answer += res * costs[i]
        i -= 1
    else:
        answer += money
        
    print(answer)
    return answer

solution(4578, [1, 4, 99, 35, 50, 1000])
solution(1999, [2, 11, 20, 100, 200, 600])
'''
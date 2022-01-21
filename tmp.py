import sys
sys.stdin = open('problem_solving\\testcase\\input.txt', 'r')
_answer_list = open('problem_solving\\testcase\\output.txt', 'r').readlines()

def swea_tc(_answer_print):
    _answer = _answer_list[0].strip()
    
    if _answer == _answer_print:
        print(f'{_answer_print} -> O')
    else:
        print(f'{_answer_print} -> X, answer: {_answer}')
        
    _answer_list.pop(0)
                
                
N = int(input())
 
for i in range(N):
    dates = int(input())
    price = list(map(int, input().split()))
    sell_price = max(price)
    total_prof = 0
    
    for j in range(dates-1):
        
        if price[j] == sell_price:
            sell_price = max(price[j+1:])
        else:
            total_prof += sell_price - price[j]
     
    
    swea_tc(f'#{i+1} {total_prof}')   
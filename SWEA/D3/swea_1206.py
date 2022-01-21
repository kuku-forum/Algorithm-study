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

# 원래 정답
swea_tc(f'#{t} {answer}')

from collections import deque

for t in range(1, 11):
    _ = int(input())
    answer = 0
    building = deque(map(int, input().split()))
    building.extendleft([0, 0])
    building.extend([0, 0])
    
    for idx in range(2, len(building) - 2):
        if building[idx - 1] >= building[idx]: continue
        if building[idx - 2] >= building[idx]: continue
        if building[idx + 1] >= building[idx]: continue
        if building[idx + 2] >= building[idx]: continue
        
        top_building = max(building[idx + 1], building[idx + 2], building[idx - 1], building[idx - 2])
        answer += building[idx] - top_building

    # answer_print = f'#{t} {answer}'
    # print(f'#{t} {answer}')
    # print(answer_print)
    
    answer_print = f'#{t} {answer}'
    swea_tc(answer_print)
    # swea_tc(f'#{t} {answer}')
from my_package.hjtc import swea_tc
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
    
    # answer_print = f'#{t} {answer}'
    # swea_tc(answer_print)
    swea_tc(f'#{t} {answer}')
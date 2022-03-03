from my_package.hjtc import swea_tc as print

from collections import deque

def max_func(numbers): 
    result = -0xffff
    for number in numbers:
        if result < number:
            result = number
    return result 


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
        
        top_building = max_func([building[idx + 1], building[idx + 2], building[idx - 1], building[idx - 2]])
        answer += building[idx] - top_building

    print(f'#{t} {answer}')
    
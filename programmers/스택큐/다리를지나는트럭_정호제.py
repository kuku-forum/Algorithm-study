from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    sum_truck = 0
    
    while bridge:
        answer += 1
        
        if bridge[0] != 0:
            sum_truck -= bridge[0]
        bridge.popleft()
        
        if trucks:
            if weight >= sum_truck + trucks[0]:
                sum_truck += trucks[0]
                bridge.append(trucks.popleft())
            else:
                bridge.append(0)
                
    return answer
#%%
'''
정확성  테스트
테스트 1 〉	통과 (1.01ms, 10.3MB)
테스트 2 〉	통과 (6.81ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (12.08ms, 10.3MB)
테스트 5 〉	통과 (74.25ms, 10.5MB)
테스트 6 〉	통과 (15.66ms, 10.3MB)
테스트 7 〉	통과 (0.72ms, 10.3MB)
테스트 8 〉	통과 (0.08ms, 10.2MB)
테스트 9 〉	통과 (1.97ms, 10.3MB)
테스트 10 〉	통과 (0.17ms, 10.3MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.28ms, 10.3MB)
테스트 13 〉	통과 (0.52ms, 10.2MB)
테스트 14 〉	통과 (0.02ms, 10.3MB)
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)], maxlen=bridge_length)
    
    total = 0
    end = len(truck_weights)
    cnt = 0
    
    while True:
        answer += 1
        truck = bridge.popleft()
        
        if truck > 0:
            total -= truck
            cnt += 1

        if trucks and weight >= total + trucks[0]:
            truck = trucks.popleft()
            bridge.append(truck)
            total += truck
        else:
            bridge.append(0)
        
        if cnt == end:
            break
        
    return answer
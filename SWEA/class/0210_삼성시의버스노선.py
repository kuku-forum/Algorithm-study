'''
버스정류장 5000
버스 노선 N, 
i번째 노선 Ai, 
Bi이하인 모든 정류장만 다님
P개의 버스 정류장에 몇개의 버스노선이 있는가

'''
from my_package.hjtc import swea_tc as print

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    AB = []
    
    for _ in range(N):
        AB.append(list(map(int, input().split())))
        
    P = int(input())
    C = []
    for _ in range(P):
        C.append(int(input()))
    
    
    bus_stop = [0 for _ in range(5001)]
    
    for a, b in AB:
        for i in range(a, b + 1):
            bus_stop[i] += 1
            
    answer = ' '.join(map(str, [bus_stop[c] for c in C]))
    
    print(f'#{t} {answer}')
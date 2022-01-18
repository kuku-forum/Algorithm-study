import sys

N = int(sys.stdin.readline())
road_list = list(map(int,sys.stdin.readline().split()))
price_list = list(map(int,sys.stdin.readline().split()))

lp = price_list[0]
answer = lp*road_list[0]

for idx in range(1, len(price_list)-1):
    if lp <= price_list[idx]: 
        answer += lp*road_list[idx]

    elif lp > price_list[idx]:
        lp = price_list[idx]
        answer += lp*road_list[idx]
    

print(answer)        
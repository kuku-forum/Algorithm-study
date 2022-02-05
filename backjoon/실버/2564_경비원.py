W, H = map(int, input().split())
N = int(input())

store_lst = []
total_length = 2*W + 2*H
# 북 남 서 동
for _ in range(N + 1):
    compass, dist = map(int, input().split())
    
    if compass == 1:
        span = dist
    elif compass == 2:
        span = W + H + W - dist
    elif compass == 3:
        span = W + H + W + H - dist
    elif compass == 4:
        span = W + dist
        
    store_lst.append(span)
    
home = store_lst.pop()
answer = 0

for store in store_lst:
    
    fowd = abs(store - home)
    back = total_length - fowd
    answer += min(fowd, back)

print(answer)
    

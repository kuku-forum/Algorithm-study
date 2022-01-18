import sys

K, N = map(int, sys.stdin.readline().split())
lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

end = max(lines)
start = 1
cnt = 0
while start <= end:
    answer = 0 
    mid = (start+end)//2
    for line in lines:
        answer += (line//mid)
    
    # print(start, end, mid, answer)

    if answer >= N:
        start = mid+1

    elif answer < N:
        end = mid-1

print(end)
        

    # if cnt ==15:
    #     break
    # cnt += 1

'''
while True:
    answer = 0 
    mid = (start+end)//2
    for line in lines:
        answer += (line//mid)
    
    print(start, end, mid, answer)

    if answer >= N:

        if start == end-1 or start == end:
            print(mid)
            break
        start = mid

    elif answer < N:
        end = mid
'''
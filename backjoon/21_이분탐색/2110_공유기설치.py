import sys

N, C = map(int, sys.stdin.readline().split())
points = []

for _ in range(N):
    points.append(int(sys.stdin.readline()))

points.sort()
start = 1 ## 최소범위부터 지정해 줘야함 1 7 8 9 10 해당예시에서 idx1-idx0을 할 경우 에러 발생
end = points[-1] - points[0]
anwer = 0
idx = 0

while start<=end:
    mid = (start+end)//2
    cnt = 1

    if start <= end:
        std_point = points[idx]
    
    for i in range(1, N):
        if points[i] - std_point >= mid:
            # print('#1', i, points[i])
            cnt += 1
            std_point = points[i]

    # print(start, end, mid, cnt, idx)

    if cnt >= C:
        start = mid+1
    elif cnt < C:
        end = mid-1

print(end)


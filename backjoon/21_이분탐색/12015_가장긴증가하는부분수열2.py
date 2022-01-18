import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
lis = []

for num in A:
    if not lis:
        lis.append(num)
    elif lis[-1] < num:
        lis.append(num)
    else:
        idx = bisect_left(lis, num)
        lis[idx] = num

print(len(lis))
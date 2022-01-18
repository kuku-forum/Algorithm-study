import sys
from bisect import bisect_left, bisect_right
N = int(sys.stdin.readline())
N_list = sorted(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = map(int, sys.stdin.readline().split())

answer = []

for target in M_list:
    answer.append(bisect_right(N_list, target)-bisect_left(N_list, target))

print(*answer, sep=' ')
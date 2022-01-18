import sys
from collections import defaultdict

N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(sys.stdin.readline())
for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    board[y -1][x - 1] = 1

L = int(sys.stdin.readline())
change = defaultdict(list)
change = {}
for _ in range(L):
    s, dir = sys.stdin.readline().split()
    change[int(s)].append(dir)


print(board)
print(change)
head, tail = [0, 0], [0, 0]
# setting = {'L':}

# while True:
#     cnt +1
# 직진 시키는걸 어떻게 할 것이었느냐
# head가 지난간 곳에 
'''
10
00

01
00

01
01
'''    
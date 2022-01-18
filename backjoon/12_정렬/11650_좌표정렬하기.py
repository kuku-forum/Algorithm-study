import sys

N = int(sys.stdin.readline())
point_2d = []
answer = []

for _ in range(N):
    point_2d.append(list(map(int, sys.stdin.readline().split())))

answer = sorted(point_2d)

for i in answer:
    print('{} {}'.format(i[0], i[1]))
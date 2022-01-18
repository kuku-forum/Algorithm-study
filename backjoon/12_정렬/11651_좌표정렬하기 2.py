import sys

N = int(sys.stdin.readline())
point_2d = []
answer = []

for _ in range(N):
    val = sys.stdin.readline().split()
    point_2d.append(list(map(int, [val[1], val[0]])))

answer = sorted(point_2d)

for i in answer:
    print('{} {}'.format(i[1], i[0]))
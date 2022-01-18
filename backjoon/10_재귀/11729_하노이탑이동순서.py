import sys

N = int(sys.stdin.readline())
steps = []

def hanoi(n, start, end, sub):
    if n == 1:
        steps.append((start, end))
    else:
        hanoi(n-1, start, sub, end)
        steps.append((start, end))
        hanoi(n-1, sub, end, start)

hanoi(N, 1, 3, 2)
print(len(steps))

for step in steps:
    print(*step, sep=' ')

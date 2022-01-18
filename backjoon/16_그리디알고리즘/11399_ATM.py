import sys

N = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

T.sort()
answer = 0
tmp = 0
for i in T:
    tmp += i
    answer.append(tmp)

# print(answer)
print(sum(answer))
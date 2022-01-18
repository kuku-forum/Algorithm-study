import sys

N = int(sys.stdin.readline())
T = []
for _ in range(N):
    T.append(int(sys.stdin.readline()))

memo = [1, 1, 1]

for num in T:
    if num == len(memo):
        print(memo[num-1])
        continue

    for i in range(len(memo), num+1):
        memo.append(memo[i-3] + memo[i-2])
    print(memo[num-1])
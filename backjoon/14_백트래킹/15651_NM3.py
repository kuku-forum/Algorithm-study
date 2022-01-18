import sys

T = list(map(int, sys.stdin.readline().split()))
N, M = T[0], T[1]
start = 1
answer = []

def dfs(s):
    if len(answer) == M:
        print(*answer, sep =' ')
        return

    for num in range(s, N+1):
        answer.append(num)
        dfs(num)
        answer.pop()
dfs(start)
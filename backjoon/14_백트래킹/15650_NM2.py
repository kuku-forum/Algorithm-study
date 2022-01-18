import sys

T = list(map(int, sys.stdin.readline().split()))
N, M = T[0], T[1]
answer = []
start = 1

def dfs(s):
    if len(answer) == M:
        print(*answer, sep=' ')
        return

    for num in range(s, N+1):
        if num not in answer:
            answer.append(num)
            dfs(num)
            answer.pop()

dfs(start)
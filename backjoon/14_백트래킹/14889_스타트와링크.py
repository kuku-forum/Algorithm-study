import sys
from itertools import combinations, permutations

N = int(sys.stdin.readline())
idx = []
table = []
scores = []
answer = []

for i in range(N):
    table.append(list(map(int, sys.stdin.readline().split())))
    idx.append(i)

teams = list(combinations(idx, N//2))
# print(teams)

for team in teams:
    tmp = list(permutations(team, 2))
    # print(tmp)
    val = 0
    for i in tmp:
        val += table[i[0]][i[1]]
    # print(val)
    scores.append(val)

for i in range(len(scores)//2):
    answer.append(abs(scores[i] - scores[len(scores)-i-1]))

print(min(answer))
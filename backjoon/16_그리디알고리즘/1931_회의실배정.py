import sys

N = int(sys.stdin.readline())
times =[]
for _ in range(N):
    times.append(list(map(int, sys.stdin.readline().split())))

times.sort(key = lambda x: (x[1], x[0]))

answer = 1
end_time = times[0][1]

for i in range(1, N):
    if times[i][0] >= end_time:
        end_time = times[i][1]
        answer += 1

print(answer)        
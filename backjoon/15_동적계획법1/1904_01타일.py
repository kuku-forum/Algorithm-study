import sys

N = int(sys.stdin.readline()) + 1

memo = [0, 1]

for i in range(2, N+1):
    tmp = (memo[i-1] + memo[i-2]) % 15746
    memo.append(tmp)

print(memo[N])







# memo = [0, 1]
# def tile(N):
#     if 2 <= N and len(memo) <= N:
#         memo.append(tile(N-2) + tile(N-1))
        
#     return memo[N]

# answer = tile(N)
# print(answer)
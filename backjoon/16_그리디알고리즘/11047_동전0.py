import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
coin_dic = {}
answer = 0

for _ in range(N):
    tmp = int(sys.stdin.readline())
    coins.append(tmp)
    coin_dic[tmp] = 0


for coin in reversed(coins):
    while K >= coin:
        K -= coin
        coin_dic[coin] += 1
        answer += 1
    
    if K == 0:
        break

print(coin_dic)
print(answer)
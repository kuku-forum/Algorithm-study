# https://nicotina04.tistory.com/65
# 이걸 어떻게 이해하지..?
import sys

N, K = map(int, sys.stdin.readline().split())
mod = 1000000007

def power(base, exp):
    if exp == 1:
        return base
    elif exp % 2 == 0:
        return (power(base, exp//2)**2) % mod
    else:
        return (power(base, exp//2)**2) * base % mod


fact = [1 for _ in range(N+1)]
for i in range(2, N+1):
    fact[i] = fact[i-1]*i%mod

A = fact[N]
B = (fact[K]*fact[N-K])%mod

result = (A * (power(B, mod-2)) % mod)

print(result)
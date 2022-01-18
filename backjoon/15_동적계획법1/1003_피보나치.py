import sys

N = int(sys.stdin.readline())

def fib(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fib(n-2) + fib(n-1))
    return memo[n]

memo = [0, 1]

for _ in range(N):
    num = int(sys.stdin.readline())
    fib(num)
    if num == 0:
        print(1, 0)
    else:
        print(memo[num-1], memo[num])

# import sys

# N = int(sys.stdin.readline())
# nums = []
# for _ in range(N):
#     nums.append(int(sys.stdin.readline()))

# def fib(n):
#     global memo
#     if n >= 2 and len(memo) <= n:
#         memo.append(fib(n-2) + fib(n-1))
#     return memo[n]

# memo = [0, 1]
# for num in nums:
#     fib(num)
#     if num == 0:
#         print(1, 0)
#     else:
#         print(memo[num-1], memo[num])



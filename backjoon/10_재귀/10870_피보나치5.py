def solve(val):
    if val >= len(memo):
        memo.append(solve(val-1) + solve(val-2))
    return memo[val]

T = int(input())

memo = [0, 1]
result = solve(T)
print(result)
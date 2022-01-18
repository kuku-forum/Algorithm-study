def solve(val):
    answer = 1
    if val < 2: return answer
    return val * solve(val-1)


T = int(input())

result = solve(T)
print(result)
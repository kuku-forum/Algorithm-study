import sys

N = int(sys.stdin.readline())
steps = []
for _ in range(N):
    steps.append(int(sys.stdin.readline()))

def stair(n):
    memo = []
    memo.append(steps[0])
    
    if n == 1:
        print(memo[-1])
        return
    
    if n == 2:
        memo.append(steps[0] + steps[1])
        print(memo[-1])
        return

    for i in range(1, 3):
        if i == 1:
            memo.append(steps[i-1] + steps[i])
        if i == 2:
            memo.append(max(steps[i-2] + steps[i], steps[i-1] + steps[i]))

    for i in range(3, n):
        memo.append(max(steps[i] + memo[i-2], steps[i] + steps[i-1] + memo[i-3]))
    
    print(memo[-1])

stair(N)


#%%
# step_rule = 0
# memo = {}
# def stair(n):
#     global memo, step_rule
    
#     # print(n)
#     if n == 1:
#         return steps[0]
#     if n == 0:
#         return 0
    
#     if (n-2, n-1) in memo:
#         pass
#     else:
#         memo[n-2, n-1] = stair(n-2) + steps[n-1]

#     if (n-1,n-1) in memo:
#         pass
#     else:
#         memo[n-1, n-1] = stair(n-1) + steps[n-1]

#     a = memo[n-2, n-1]
#     b = memo[n-1, n-1]
    
#     if b > a:
#         step_rule += 1
    
#     if step_rule == 2:
#         step_rule = 0
#         return a
        
#     return max(a, b)

# answer = stair(N)
# print(answer)
import sys

N = int(sys.stdin.readline())
PS_list = []

for _ in range(N):
    PS_list.append(sys.stdin.readline().rstrip())

for PS in PS_list:
    stack = []
    for S in PS:
        if not stack:
            stack.append(S)
        
        elif stack[-1] == '(' and S == ')':
            stack.pop()
        else:
            stack.append(S)
    
    if not stack: print('YES')
    else: print('NO')
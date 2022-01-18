import sys

N = int(sys.stdin.readline())
que = list(map(int, sys.stdin.readline().split()))

answer = [-1 for _ in range(N)]
stack = []

for i, j in enumerate(que):
    
    print(stack)

    while True:
        if not stack:
            stack.append([i,j])
            break
        else: 
            if j > stack[-1][1]:
                tmp = stack.pop()
                answer[tmp[0]] = j
            else:
                stack.append([i,j]) 
                break

print(*answer, sep=' ')
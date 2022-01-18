'''
1 2 3 4 5
+ 1
- 1
+ 2
- 1 (2)
+ 3 4 5
- 1 2 (5)
+ 3 4
1 2 5 3 4

1 2 3 4 5 6 7 8
+ 1 2 3 4
- (4 3)
+ 1 2 (5 6)
- 4 3 (6)
+ 1 2 5 7 8
- 4 3 6 (8 7 5 2 1)
4 3 6 8 7 5 2 1
'''
import sys

N = int(sys.stdin.readline())

seq = []
for _ in range(N):
    seq.append(int(sys.stdin.readline()))

stack = []
i = 1
answer = []
while True:

    if not stack:
        stack.append(i)
        answer.append('+')
        i += 1
    elif stack[-1] == seq[0]:
        stack.pop()
        seq.pop(0)
        answer.append('-')
    else:
        stack.append(i)
        answer.append('+')
        i += 1
    # print(i, answer, stack, seq)

    if not seq:
        for i in answer:
            print(i)
        break
    elif i == N+1 and stack[-1] != seq[0]:
        print('NO')
        break
    
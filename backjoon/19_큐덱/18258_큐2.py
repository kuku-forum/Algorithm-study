import sys
from collections import deque

N = int(sys.stdin.readline())
command_list = []
queue = deque()

for _ in range(N):
    command_list.append(sys.stdin.readline().split())

def push(n):
    queue.append(n)

def pop():
    if not queue: print(-1)
    else: print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if not queue: print(1)
    else: print(0)
        
def front():
    
    if not queue: print(-1)
    else: print(queue[0])

def back():
    if not queue: print(-1)
    else: print(queue[-1])    


for command in command_list:
    func = command[0]
    if func == "empty": empty()
    elif func == "push": push(command[1])
    elif func == "pop": pop()
    elif func == "size": size()
    elif func == "front": front()
    elif func == "back": back()


''' 함수 호출로 인한 시간복잡도 차이 발생
import sys
from collections import deque
num = int(sys.stdin.readline())
q = deque([])
for i in range(num):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
'''
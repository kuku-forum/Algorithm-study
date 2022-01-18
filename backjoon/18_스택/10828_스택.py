import sys

N = int(sys.stdin.readline())
command_list = []
stack = []

for _ in range(N):
    command_list.append(sys.stdin.readline().split())

def empty():
    if len(stack) == 0: print(1)
    else: print(0)
        
def push(n):
    stack.append(n)

def pop():
    if len(stack) == 0: print(-1)
    else: print(stack.pop(-1))
    
def size():
    print(len(stack))

def top():
    if len(stack) == 0: print(-1)
    else: print(stack[-1])

for command in command_list:
    func = command[0]
    if func == "empty": empty()
    elif func == "push": push(command[1])
    elif func == "pop": pop()
    elif func == "size": size()
    elif func == "top": top()




# for _ in range(N):
#     T = sys.stdin.readline().split()
#     command = T[0]
#     if command == "empty": empty()
#     elif command == "push": push(T[1])
#     elif command == "pop": pop()
#     elif command == "size": size()
#     elif command == "top": top()
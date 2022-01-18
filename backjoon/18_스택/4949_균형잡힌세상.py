'''

So when I die (the [first] I will see in (heaven) is a score list).     yes
[ first in ] ( first out ).     yes
Half Moon tonight (At least it is better than no Moon at all].      no
A rope may form )( a trail in a maze.   no
Help( I[m being held prisoner in a fortune cookie factory)]. no
([ (([( [ ] ) ( ) (( ))] )) ]).     yes
 .      yes
.
'''

import sys

line_list = []
while True:
    T = sys.stdin.readline().rstrip()
    if T == '.': break
    else: line_list.append(T)

for line in line_list:
    stack = []
    for char in line:
        if char == '(' or char == ')' or char == '[' or char == ']':
            if not stack: stack.append(char)
            elif stack[-1] == '(' and char == ')': stack.pop()
            elif stack[-1] == '[' and char == ']': stack.pop()
            else: stack.append(char)
    
    if not stack: print('yes')
    else: print('no')

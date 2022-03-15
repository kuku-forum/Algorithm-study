from my_package.hjtc import swea_tc as print
T = 11

from collections import deque

def in_to_post_order(fomula):
    oper_dic = {'(': 0, 
                '+': 1, '-': 1,
                '*': 2, '/': 2}
    
    stack = []
    convert_fomula = []
    
    
    while fomula:
        node = fomula.popleft()
        
        if node.isdigit():
            convert_fomula.append(node)
        else:
            if node == '(' :
                stack.append(node)
            elif node == ')':
                while stack[-1] != '(':
                  convert_fomula.append(stack.pop())
                stack.pop() 
            
            else:
                while stack and oper_dic[node] <= oper_dic[stack[-1]]:
                    convert_fomula.append(stack.pop())
                stack.append(node)
    
    while stack: 
        convert_fomula.append(stack.pop())
        
    return convert_fomula


def calc(convert_fomula):
    stack = []
    
    for i in range(len(convert_fomula)):
        node = convert_fomula[i]
        
        if node.isdigit():
            stack.append(node)
            
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if node == '+':
                stack.append(num1 + num2)
                
            elif node == '-':
                stack.append(num1 - num2)
                
            elif node == '*':
                stack.append(num1 * num2)
                
            elif node == '/':
                stack.append(num1 / num2)
    
    return stack[-1]
    

for t in range(1, 11):
    answer = 0
    
    N = int(input())
    fomula = deque(input())

    convert_fomula = in_to_post_order(fomula)
    answer = calc(convert_fomula)
    
    print(f'#{t} {answer}')
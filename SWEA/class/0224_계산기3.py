from my_package.hjtc import swea_tc as print

T = 11
for t in range(1, T):
    answer = 0
    
    N = int(input())
    fomula = list(reversed(input()))
    
    oper_dic = {'+': 1,
                '-': 1,
                '*': 2,
                '/': 2,
                '(': 0}
    
    # print(fomula)
    
    stack = []
    convert_fomula = []
    
    while fomula:
        node = fomula.pop()
        
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
                    
    while len(stack) != 0: 
        convert_fomula.append(stack.pop())
    
    answer = 0
    
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
                
    print(f'#{t} {stack[-1]}')
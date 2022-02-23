from my_package.hjtc import swea_tc as print
# from my_package.hjtc import swea_tc

for t in range(1, int(input()) + 1):
    answer = []
    
    expression = list(reversed(input()))
    stk = []
    operator_dic = {'*': 2,
                    '+': 1}
    
    for _ in range(len(expression)):
        element = expression.pop()
        if element.isdigit():
            answer.append(element)
        else:
            if not stk:
                stk.append(element)
            else:
                if operator_dic[element] > operator_dic[stk[-1]]:
                    stk.append(element)
                else:
                    while stk and operator_dic[element] <= operator_dic[stk[-1]]:
                        answer.append(stk.pop())
                    stk.append(element)
                    
    while stk:
        answer.append(stk.pop())
    
    print(f'#{t} {"".join(map(str, answer))}')
    
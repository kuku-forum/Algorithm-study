for t in range(1, int(input()) + 1):
    events = list(reversed(input().split()))
    stack = []
    answer = 'error'
    
    while events:
        event = events.pop()
        
        if event[-1].isdigit():
            stack.append(event)
        
        elif event == '.':
            if len(stack) == 1:
                answer = stack.pop()
            else:
                answer = 'error'
            break
        
        else:
            if len(stack) >= 2:
                num2 = stack.pop()
                num1 = stack.pop()
            else:
                answer = 'error'
                break
            
            if num1[-1].isdigit() and num2[-1].isdigit():
                if event == '+':
                    eval_num = int(num1) + int(num2)
                elif event == '-':
                    eval_num = int(num1) - int(num2)
                elif event == '*':
                    eval_num = int(num1) * int(num2)
                elif event == '/':
                    if int(num2) == 0:
                        answer = 'error'
                        break
                    eval_num = int(num1) // int(num2)
                        
                stack.append(str(eval_num))
                
            else:
                answer = 'error'
                break
            
    print(f'#{t} {answer}')
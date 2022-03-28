

def dfs(i, num3, length):
    if i == length:
        return
    
    if num3[i]=='0':
        num3_list.append(int(num3[:i]+'1'+num3[i+1:],3))
        num3_list.append(int(num3[:i]+'2'+num3[i+1:],3))
        
    elif num3[i]=='1':
        if i != 0:
            num3_list.append(int(num3[:i]+'0'+num3[i+1:],3))
        num3_list.append(int(num3[:i]+'2'+num3[i+1:],3))
    else:
        
        if i!= 0:
            num3_list.append(int(num3[:i]+'0'+num3[i+1:],3))
        num3_list.append(int(num3[:i]+'1'+num3[i+1:],3))
        
    dfs(i+1, num3, length)

T = int(input())
for tc in range(1, T+1):
    num2 = input()
    length2 = len(num2)
    num2 = int(num2,2)
    num3 = input()
    length = len(num3)
    num3_list = []
    
    print(num2, type(num2))
    dfs(0, num3, length)
    ans = 0
    
    for x in num3_list:
        if length2 < len(bin(x)[2:]): 
            continue
        
        now = abs(num2 - x)
        
        while now:
            if now%2 ==0:
                now //= 2
            else:
                if now == 1:
                    ans = x
                    break
                break
        if ans !=0:
            break
        
    print(f'#{tc} {ans}')
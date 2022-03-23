def bi2deci(num):
    result = 0
    for i in range(len(num)):
        result += int(num[len(num)-i-1])*pow(2,i)
    return result


def hex2bin(num):
    global tmp
    if num == 0:
        return
    q, r = divmod(num, 2)
    hex2bin(q)
    tmp += str(r)
    
    
for t in range(1, int(input()) + 1):
    info = list(input())
    new_info = []
    answer = []
    hex_dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    
    for num in info:
        tmp = ''
        if num.isdigit():
            hex2bin(int(num))
        else:
            hex2bin(hex_dic[num])
        tmp = tmp.zfill(4)
        new_info += list(tmp)
    
    for i in range(0, len(new_info), 7):
        answer.append(bi2deci(new_info[i:i+7]))
        
    print(f'#{t}', *answer)

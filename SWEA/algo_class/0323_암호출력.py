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
    new_info = ''
    answer = []
    hex_dic = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    password_dic = {
        '001101': 0,
        '010011': 1,
        '111011': 2,
        '110001': 3,
        '100011': 4,
        '110111': 5,
        '001011': 6,
        '111101': 7,
        '011001': 8,
        '101111': 9,
    }
    
    for num in info:
        tmp = ''
        if num.isdigit():
            hex2bin(int(num))
        else:
            hex2bin(hex_dic[num])
        tmp = tmp.zfill(4)
        new_info += (tmp)
    
    start = 0 
    flag = False
    while len(new_info) > start:
        pattern = ''
        for idx in range(start, start+6):
            if idx >= len(new_info):
                flag = True
                break
            pattern += new_info[idx]
        else:
            if pattern in password_dic:
                answer.append(password_dic[pattern])
                start += 6
            else:
                start += 1
            
        if flag:
            break
            
    print(f'#{t}', *answer)

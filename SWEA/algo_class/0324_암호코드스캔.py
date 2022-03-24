from my_package.hjtc import swea_tc # as print

from collections import deque

hex_dic = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

password_short_dic = {
    '211': '0', '221': '1', '122': '2', '411': '3', '132': '4',
    '231': '5', '114': '6', '312': '7', '213': '8', '112': '9',
}

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    answer = 0 
    board = set()
    result = set()
    rm_row = '0'*M
    info = []
    
    for _ in range(N):
        board.add(input().rstrip('0'))
    
    for row in board:
        # row = row.rstrip('0')
        tmp_row = ''
        
        for r in row:
            tmp_row += hex_dic[r]
        if tmp_row:
            info.append(tmp_row)
    
    for row in info:
        flag = False
        prev = '1'
        que = deque([])
        cnt = 0
        tmp_result = ''
        
        for i in range(len(row)-1, -1, -1):
            
            if not flag and row[i] == '1':
                flag = True
                cnt += 1
                
            elif flag:
                if row[i] == prev:
                    cnt += 1
                else:
                    que.appendleft(str(cnt))
                    prev = str(row[i])
                    cnt = 1
                    
            if len(que) == 4:
                min_val = int(min(map(int, que)))
                if int(min_val) > 1:
                    for i in range(1, 4):
                        que[i] = str(int(que[i])//min_val)
                tmp_result = password_short_dic[''.join((que[1], que[2], que[3]))] + tmp_result
                
                if len(tmp_result) == 8:
                    result.add(tmp_result)
                    tmp_result = ''
                que = deque([])
                
        else:
            min_val = int(min(map(int, que)))
            if int(min_val) > 1:
                for i in range(3):
                    que[i] = str(int(que[i])//min_val)
            
            tmp_result = password_short_dic[''.join((que[0], que[1], que[2]))] + tmp_result
            result.add(tmp_result)
            
    for row in result:
        ssum = (int(row[0]) + int(row[2]) + int(row[4]) + int(row[6]))*3 + (int(row[1]) + int(row[3]) + int(row[5])) + int(row[7])
        
        if ssum%10 == 0:
            answer += sum(map(int, row))
        
    print(f'#{t} {answer}')
from my_package.hjtc import swea_tc # as print

def solution(board):
    
    for row in board:
        result = []
        end = len(row)-1
        flag = False
        while end >= 0 :
            pattern = ''
            for idx in range(end, end-7, -1):
                if 0 > idx:
                    flag = True
                    break
                pattern = row[idx] + pattern
            else:
                if pattern in password_dic:
                    result.append(password_dic[pattern])
                    end -= 7
                else:
                    end -= 1
                
            if flag:
                break
        
        if len(result) == 8:
            odd_sum = 0
            even_sum = 0
            for i, num in enumerate(result[::-1][:-1]):
                
                if (i+1)%2 == 0:
                    even_sum += num
                else:
                    odd_sum += num
                    
            total_num = odd_sum*3 + even_sum + result[0]
            
            if total_num%10 == 0:
                return sum(result)
            else:
                return 0
    
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    
    info = [list(input()) for _ in range(N)]
    password_dic = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
        '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9,
    }
    
    print(f'#{t}', solution(info))
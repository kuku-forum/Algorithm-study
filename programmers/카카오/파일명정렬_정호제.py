'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.4MB)
테스트 2 〉	통과 (0.03ms, 10.5MB)
테스트 3 〉	통과 (3.06ms, 11MB)
테스트 4 〉	통과 (2.88ms, 10.9MB)
테스트 5 〉	통과 (3.61ms, 10.8MB)
테스트 6 〉	통과 (2.81ms, 10.9MB)
테스트 7 〉	통과 (2.77ms, 10.8MB)
테스트 8 〉	통과 (2.51ms, 11MB)
테스트 9 〉	통과 (2.59ms, 10.7MB)
테스트 10 〉	통과 (2.57ms, 10.7MB)
테스트 11 〉	통과 (2.60ms, 10.6MB)
테스트 12 〉	통과 (2.82ms, 10.8MB)
테스트 13 〉	통과 (3.70ms, 10.8MB)
테스트 14 〉	통과 (2.96ms, 11.2MB)
테스트 15 〉	통과 (3.00ms, 11.2MB)
테스트 16 〉	통과 (4.01ms, 10.9MB)
테스트 17 〉	통과 (2.26ms, 10.9MB)
테스트 18 〉	통과 (2.35ms, 10.8MB)
테스트 19 〉	통과 (2.80ms, 10.8MB)
테스트 20 〉	통과 (2.80ms, 10.8MB)
'''
def solution(files):
    answer = []
    name_lst = []
    
    for file in files:
        start = False
        end = False
        
        for i in range(len(file)):
            if file[i].isdigit() and start == False:
                start = i
            
            if not file[i].isdigit() and start != False:
                end = i
                break
        else:
            head = file[:start]
            number = file[start:]
            tail = ''
            name_lst.append([head, number, tail])
            continue
                
        head = file[:start]
        number = file[start:end]
        tail = file[end:]
        name_lst.append([head, number, tail])
    
    name_lst.sort(key = lambda x: (x[0].lower(), int(x[1])))
    
    
    return [''.join(name) for name in name_lst]

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.05ms, 10.4MB)
테스트 3 〉	통과 (5.19ms, 10.9MB)
테스트 4 〉	통과 (3.68ms, 10.9MB)
테스트 5 〉	통과 (2.95ms, 10.8MB)
테스트 6 〉	통과 (2.73ms, 10.8MB)
테스트 7 〉	통과 (2.84ms, 10.9MB)
테스트 8 〉	통과 (2.40ms, 11MB)
테스트 9 〉	통과 (4.27ms, 10.7MB)
테스트 10 〉	통과 (2.50ms, 10.9MB)
테스트 11 〉	통과 (2.50ms, 10.8MB)
테스트 12 〉	통과 (5.51ms, 10.8MB)
테스트 13 〉	통과 (2.72ms, 10.7MB)
테스트 14 〉	통과 (6.46ms, 11.1MB)
테스트 15 〉	통과 (6.41ms, 11.1MB)
테스트 16 〉	통과 (3.05ms, 10.8MB)
테스트 17 〉	통과 (2.21ms, 10.8MB)
테스트 18 〉	통과 (2.30ms, 10.9MB)
테스트 19 〉	통과 (2.83ms, 10.8MB)
테스트 20 〉	통과 (5.35ms, 10.8MB)
'''
def solution(files):
    HNT = []
    
    for i, file in enumerate(files):
        HEAD, NUMBER = True, True
        head, number, tail = '', '', ''
        
        for i, factor in enumerate(file):
            if not factor.isdigit() and HEAD == True:
                head += factor
                
            elif factor.isdigit() and NUMBER == True:
                HEAD = False
                number += factor
                
            else:
                NUMBER = False
                tail += factor    
                
        HNT.append([head, number, tail])
                
    return [''.join(split_str) for split_str in sorted(HNT, key = lambda x: (x[0].lower(), int(x[1])))]



'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.5MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.03ms, 10.5MB)
테스트 5 〉	통과 (0.03ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.5MB)
테스트 7 〉	통과 (0.03ms, 10.5MB)
테스트 8 〉	통과 (0.03ms, 10.4MB)
테스트 9 〉	통과 (0.03ms, 10.4MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.03ms, 10.4MB)
테스트 12 〉	통과 (0.03ms, 10.5MB)
테스트 13 〉	통과 (0.03ms, 10.5MB)
테스트 14 〉	통과 (0.03ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.5MB)
테스트 16 〉	통과 (0.03ms, 10.4MB)
테스트 17 〉	통과 (0.03ms, 10.5MB)
테스트 18 〉	통과 (0.03ms, 10.5MB)
테스트 19 〉	통과 (0.04ms, 10.5MB)
테스트 20 〉	통과 (0.03ms, 10.4MB)
테스트 21 〉	통과 (0.03ms, 10.4MB)
테스트 22 〉	통과 (0.03ms, 10.4MB)
테스트 23 〉	통과 (0.03ms, 10.4MB)
테스트 24 〉	통과 (0.03ms, 10.5MB)
테스트 25 〉	통과 (0.03ms, 10.4MB)
테스트 26 〉	통과 (0.03ms, 10.4MB)
테스트 27 〉	통과 (0.03ms, 10.5MB)
테스트 28 〉	통과 (0.04ms, 10.5MB)
테스트 29 〉	통과 (0.03ms, 10.4MB)
테스트 30 〉	통과 (0.03ms, 10.5MB)
테스트 31 〉	통과 (0.03ms, 10.4MB)
테스트 32 〉	통과 (0.03ms, 10.4MB)
'''
def solution(dartResult):
    answer = []
    i = 0
    
    while True:
        if i == len(dartResult):
            break
            
        if dartResult[i].isdigit():
            if dartResult[i+1].isdigit():
                score = int(dartResult[i:i+2])
                i += 1
            else:
                score = int(dartResult[i])
            
            if len(dartResult) > i + 1:
                bonus = dartResult[i + 1]
                
            option = ''
            
            if len(dartResult) > i+2 :
                if dartResult[i+2] == '#' or dartResult[i+2] == '*':
                    option = dartResult[i+2]
                
            print(score, bonus, option)
            
            if bonus == 'D':
                score = score**2
            elif bonus == 'T':
                score = score**3
            
            if option:
                # if i == 0:
                #     score *= 2
                if option == '*':
                    if answer:
                        answer[-1] *= 2
                    score *= 2
                else:
                    score *= -1
                    
            # print(score)
            answer.append(score)
            
        i += 1
        
    print(answer)
    return sum(answer)
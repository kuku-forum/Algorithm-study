'''
정확성  테스트
테스트 1 〉	통과 (0.17ms, 10.4MB)
테스트 2 〉	통과 (7.40ms, 10.9MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (15.60ms, 12.3MB)
테스트 5 〉	통과 (4.11ms, 10.7MB)
테스트 6 〉	통과 (1.30ms, 10.5MB)
테스트 7 〉	통과 (5.60ms, 11MB)
테스트 8 〉	통과 (0.07ms, 10.3MB)
테스트 9 〉	통과 (137.06ms, 10.6MB)
테스트 10 〉	통과 (147.76ms, 10.4MB)
테스트 11 〉	통과 (169.88ms, 10.4MB)
테스트 12 〉	통과 (209.47ms, 10.7MB)
테스트 13 〉	통과 (203.49ms, 10.8MB)
테스트 14 〉	통과 (188.15ms, 10.8MB)
테스트 15 〉	통과 (182.71ms, 10.3MB)
테스트 16 〉	통과 (152.11ms, 10.4MB)
테스트 17 〉	통과 (183.91ms, 10.6MB)
테스트 18 〉	통과 (172.31ms, 10.9MB)
테스트 19 〉	통과 (175.41ms, 10.4MB)
테스트 20 〉	통과 (134.28ms, 10.3MB)
테스트 21 〉	통과 (143.46ms, 10.9MB)
테스트 22 〉	통과 (0.06ms, 10.4MB)
테스트 23 〉	통과 (0.05ms, 10.3MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.06ms, 10.4MB)
테스트 26 〉	통과 (0.07ms, 10.3MB)
테스트 27 〉	통과 (0.02ms, 10.3MB)
테스트 28 〉	통과 (0.03ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
'''
from itertools import combinations

def solution(line):
    answer = []
    point_lst = set()
    
    for line_1, line_2 in combinations(line, 2):
        a, b, e = line_1
        c, d, f = line_2
        
        denominator = a*d - b*c
        
        if denominator == 0:
            continue
        X = (b*f - e*d)/denominator
        Y = (e*c - a*f)/denominator
        
        if X == int(X) and Y == int(Y):
            point_lst.add((int(Y), int(X)))
    
    point_lst = sorted(point_lst, key = lambda x : x[1])
    width = abs(point_lst[0][1] - point_lst[-1][1]) + 1
    x_min = point_lst[0][1]
    
    point_lst = sorted(point_lst, key = lambda x : -x[0])
    y_max = point_lst[0][0]
    y_min = point_lst[-1][0]
    
    print(point_lst)
    for num in range(y_max, y_min-1, -1):
        if not point_lst:
            break
        
        row = ['.' for _ in range(width)]
        
        while True:
            if not point_lst:
                break
                
            if point_lst[0][0] == num:
                point = point_lst.pop(0)
                row[point[1] - x_min] = '*'
            else:
                break
                
        answer.append(''.join(row))

    return answer
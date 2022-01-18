'''
정확성  테스트
테스트 1 〉	통과 (0.07ms, 10.3MB)
테스트 2 〉	통과 (0.07ms, 10.3MB)
테스트 3 〉	통과 (0.08ms, 10.3MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (0.08ms, 10.3MB)
테스트 6 〉	통과 (0.35ms, 10.2MB)
테스트 7 〉	통과 (0.21ms, 10.3MB)
테스트 8 〉	통과 (1.88ms, 10.3MB)
테스트 9 〉	통과 (1.26ms, 10.4MB)
테스트 10 〉	통과 (1.56ms, 10.5MB)
테스트 11 〉	통과 (0.84ms, 10.4MB)
테스트 12 〉	통과 (0.97ms, 10.4MB)
테스트 13 〉	통과 (1.47ms, 10.5MB)
테스트 14 〉	통과 (0.91ms, 10.4MB)
테스트 15 〉	통과 (1.54ms, 10.5MB)
테스트 16 〉	통과 (0.35ms, 10.3MB)
테스트 17 〉	통과 (0.20ms, 10.4MB)
테스트 18 〉	통과 (0.09ms, 10.3MB)
테스트 19 〉	통과 (0.03ms, 10.3MB)
테스트 20 〉	통과 (0.27ms, 10.3MB)
'''
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    menu_dic = defaultdict(int)
    course_dic = defaultdict(list)
    
    for i in course:
        for order in orders:
            order = sorted(order)
            for menu in combinations(order, i):
                menu_dic[''.join(menu)] += 1
                
    for menu, cnt in menu_dic.items():
        if cnt == 1:
            continue
        course_dic[len(menu)].append([menu, cnt])
    
    for i in course:
        course_dic[i].sort(key = lambda x: -x[1])
        
        if not course_dic[i]:
            continue
        
        answer.append(course_dic[i][0][0])
        max_num = course_dic[i][0][1]

        for course_menu in course_dic[i][1:]:
            if course_menu[1] == max_num:
                answer.append(course_menu[0])
            else:
                break
                
    return sorted(answer)


'''

정확성  테스트
테스트 1 〉	통과 (0.19ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.2MB)
테스트 3 〉	통과 (0.11ms, 10.3MB)
테스트 4 〉	통과 (0.11ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.4MB)
테스트 6 〉	통과 (0.26ms, 10.2MB)
테스트 7 〉	통과 (0.45ms, 10.3MB)
테스트 8 〉	통과 (2.68ms, 10.5MB)
테스트 9 〉	통과 (1.73ms, 10.3MB)
테스트 10 〉	통과 (2.94ms, 10.6MB)
테스트 11 〉	통과 (1.26ms, 10.4MB)
테스트 12 〉	통과 (2.42ms, 10.4MB)
테스트 13 〉	통과 (2.03ms, 10.7MB)
테스트 14 〉	통과 (1.55ms, 10.5MB)
테스트 15 〉	통과 (2.15ms, 10.7MB)
테스트 16 〉	통과 (0.99ms, 10.5MB)
테스트 17 〉	통과 (0.31ms, 10.3MB)
테스트 18 〉	통과 (0.23ms, 10.2MB)
테스트 19 〉	통과 (0.04ms, 10.2MB)
테스트 20 〉	통과 (0.40ms, 10.3MB)

'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for i in course:
        candidates = []
        
        for order in orders:
            for case in combinations(order, i):
                candidates.append(''.join(sorted(case)))
        print(candidates)
        sorted_candidates = Counter(candidates).most_common()
        
        for menu, cnt in sorted_candidates:
            if cnt > 1 and cnt == sorted_candidates[0][1]:
                answer.append(menu)
    
    return sorted(answer)
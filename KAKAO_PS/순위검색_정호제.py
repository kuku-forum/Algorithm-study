'''
정확성  테스트
테스트 1 〉	통과 (0.15ms, 10.5MB)
테스트 2 〉	통과 (0.16ms, 10.5MB)
테스트 3 〉	통과 (0.26ms, 10.4MB)
테스트 4 〉	통과 (1.25ms, 10.6MB)
테스트 5 〉	통과 (1.65ms, 10.5MB)
테스트 6 〉	통과 (2.98ms, 10.5MB)
테스트 7 〉	통과 (2.42ms, 10.7MB)
테스트 8 〉	통과 (25.35ms, 11.5MB)
테스트 9 〉	통과 (25.48ms, 11.6MB)
테스트 10 〉	통과 (25.92ms, 11.7MB)
테스트 11 〉	통과 (1.68ms, 10.6MB)
테스트 12 〉	통과 (3.04ms, 10.6MB)
테스트 13 〉	통과 (2.42ms, 10.8MB)
테스트 14 〉	통과 (12.94ms, 11MB)
테스트 15 〉	통과 (13.04ms, 11MB)
테스트 16 〉	통과 (1.64ms, 10.6MB)
테스트 17 〉	통과 (3.03ms, 10.6MB)
테스트 18 〉	통과 (12.73ms, 11MB)
효율성  테스트
테스트 1 〉	통과 (445.57ms, 42.5MB)
테스트 2 〉	통과 (401.92ms, 42.7MB)
테스트 3 〉	통과 (421.85ms, 42.6MB)
테스트 4 〉	통과 (425.75ms, 42.3MB)
'''
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dic = defaultdict(list)
    
    for sentence in info:
        raw_data = sentence.split()
        data = raw_data[:-1]
        num = int(raw_data[-1])
        
        for i in range(5):
            for com_data in combinations(data, i):
                info_dic[com_data].append(num)
    
    for key in info_dic.keys():
        info_dic[key].sort()
    
    for que in query:
        que_split = que.replace('-', '').replace('and', '').split()
        num_lst = info_dic[tuple(que_split[:-1])]
        answer.append(len(num_lst) - bisect_left(num_lst, int(que_split[-1])))
        
    return answer

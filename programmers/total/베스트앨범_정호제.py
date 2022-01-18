from collections import defaultdict

def solution(genres, plays):
    answer = []
    gen_dict = defaultdict(int)
    play_dict = defaultdict(list)
    
    for i, factor in enumerate(zip(genres, plays)):
        
        gen_dict[factor[0]] += factor[1]
        play_dict[factor[0]].append([i, factor[1]])
    
    gen_order = sorted(gen_dict, key = lambda x : -gen_dict[x])
    
    for order in gen_order:
        tmp = sorted(play_dict[order], key = lambda x : (-x[1], x[0]))
        
        if len(tmp) > 1:
            for i, _ in tmp[:2]:
                answer.append(i)
        else:
            answer.append(tmp[0][0])
            
    return answer

#%%
'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.09ms, 10.2MB)
테스트 6 〉	통과 (0.06ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.05ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.3MB)
테스트 10 〉	통과 (0.07ms, 10.2MB)
테스트 11 〉	통과 (0.02ms, 10.2MB)
테스트 12 〉	통과 (0.04ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.07ms, 10.3MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
'''
from collections import defaultdict

def solution(genres, plays):
    answer = []
    gen_dic = defaultdict(dict)
    gen_cnt = defaultdict(int)
    
    idx = 0
    for gen, play in zip(genres, plays):
        gen_dic[gen].update({idx: play}) 
        gen_cnt[gen] += play
        idx += 1
    
    name_lst = sorted(gen_cnt, key = lambda x: gen_cnt[x], reverse=True)
    
    for name in name_lst:
        answer.extend(sorted(gen_dic[name], key = lambda x: gen_dic[name][x], reverse=True)[:2])
    
    return answer
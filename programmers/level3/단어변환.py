'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.2MB)
테스트 2 〉	통과 (3.59ms, 10.3MB)
테스트 3 〉	통과 (3.92ms, 10.3MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.2MB)
'''
from collections import Counter, defaultdict, deque

def solution(begin, target, words):
    answer = 0
    
    init_lst = []
    
    que = deque()
    que.append(begin)
    repeat_chk = defaultdict(int)
    target_cnt = Counter(target)
    
    while que:    
        for _ in range(len(que)):
            start = que.popleft()
            repeat_chk[start] += 1
            print(que)
            for word in words:
                start_cnt = Counter(start)
                word_cnt = Counter(word)
                sub_word_cnt = start_cnt - word_cnt
                sub_target_cnt = start_cnt - target_cnt

                if len(sub_target_cnt) == 0:
                    return answer

                elif len(sub_word_cnt) == 1:
                    for key in sub_word_cnt:
                        if sub_word_cnt[key] != 1:
                            continue
                            
                    if repeat_chk[word] == 0:
                        repeat_chk[word] += 1
                        que.append(word)
        answer += 1
    return 0
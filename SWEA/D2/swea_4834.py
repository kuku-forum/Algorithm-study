from collections import Counter

T = int(input())

for t in range(1, T + 1):
    _ = input()
    
    a_str = input()
    a_cnt = Counter(a_str).most_common()
    a_cnt.sort(key = lambda x: (-x[1], -int(x[0])))
    answer = ' '.join(map(str, a_cnt[0]))
    print(f'#{t} {answer}')
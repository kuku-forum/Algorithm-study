T = int(input())

def solution(word):
    mid_pos = len(word)//2
    
    if len(word) % 2 == 0:
        bacward = range(mid_pos-1, -1, -1)
        forward = range(mid_pos, len(word))
        
        for i, j in zip(bacward, forward):
            if word[i] != word[j]:
                return 0
    else:
        bacward = range(mid_pos-1, -1, -1)
        forward = range(mid_pos+1, len(word))
        
        for i, j in zip(bacward, forward):
            if word[i] != word[j]:
                return 0
    return 1

for t in range(1, T+1):
    print(f'#{t} {solution(input())}')
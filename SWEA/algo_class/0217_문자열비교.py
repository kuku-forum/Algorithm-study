def solution(word1, word2):
    for i in range(len(word2) - len(word1) + 1):
        for j, k in enumerate(range(i, i + len(word1))):
            if word2[k] != word1[j]:
                break
        else:
            return 1
        
    return 0


T = int(input())

for t in range(1, T+1):
    word1 = input()
    word2 = input()
    
    print(f'#{t} {solution(word1, word2)}')
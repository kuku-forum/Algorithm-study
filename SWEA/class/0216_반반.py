for t in range(1, int(input()) + 1):
    word = input().strip()
    word_set = list(set(word.strip()))
    answer = 'No'
    
    if len(word_set) == 2:
        for i in range(2):
            cnt = 0
            for alp in word:
                if word_set[i] == alp:
                    cnt += 1
            if cnt != 2:
                break        
        else:
            answer = 'Yes'
    
    print(f'#{t} {answer}')
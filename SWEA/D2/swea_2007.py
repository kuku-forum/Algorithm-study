T = int(input())

for t in range(1, T+1):
    answer = 0
    sentence = input()
    sen_len = len(sentence)
    
    for div in range(1, 11):
        start = 0
        word = sentence[start:start+div]
        
        while sen_len > start+div:
            
            if word != sentence[start:start+div]:
                break
            start += div
        else:
            answer = div
            break

    print(f'#{t} {answer}')
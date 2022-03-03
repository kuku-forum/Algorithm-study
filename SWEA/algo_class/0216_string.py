from my_package.hjtc import swea_tc as print

for t in range(1, 11):
    
    _ = int(input())
    word = input()
    sentence = input()
    
    answer = 0
    
    for i in range(len(sentence) - len(word) + 1):
        for j in range(len(word)):
            if sentence[i + j] != word[j]:
                break
        else:
            answer += 1
            
    
    print(f'#{t} {answer}')
        
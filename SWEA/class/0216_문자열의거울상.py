'''
bdppq
qppdb

pqqbd
'''


for t in range(1, int(input()) + 1):
    alp_dic ={'q': 'p', 'p': 'q', 'd': 'b', 'b': 'd'}
    word = input()
    answer = ''
    
    for i in range(len(word) - 1, -1, -1):
        answer += alp_dic[word[i]]
        
    print(f'#{t} {answer}')
    
    
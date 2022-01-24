from my_package.hjtc import swea_tc

T = int(input())

for t in range(1, T + 1):
    new_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    word_to_num = {word: num for num, word in enumerate(new_num)}
    num_to_word = {num: word for num, word in enumerate(new_num)}
    
    _, N = input().split()
    
    
    num_list = [word_to_num[word] for word in input().split()]
    word_list = [num_to_word[num] for num in sorted(num_list)]
    
    answer = ' '.join(word_list)
    swea_tc(f'#{t}')
    swea_tc(f'{answer}')
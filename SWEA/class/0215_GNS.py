from my_package.hjtc import swea_tc 


T = int(input())

def bubbleSort(arr):
    
    length = len(arr) - 1
    
    for i in range(length):
        for j in range(length-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

for t in range(1, T + 1):
    new_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    word_to_num = {word: num for num, word in enumerate(new_num)}
    num_to_word = {num: word for num, word in enumerate(new_num)}
    _, N = input().split()
    
    print(word_to_num)
    print(num_to_word)
    num_list = [word_to_num[word] for word in input().split()]
    word_list = [num_to_word[num] for num in bubbleSort(num_list)]
    
    answer = ' '.join(word_list)
    # print(f'#{t}')
    # print(f'{answer}')
    
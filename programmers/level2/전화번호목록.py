'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.00ms, 10.1MB)
테스트 5 〉	통과 (0.00ms, 10.1MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.2MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.40ms, 10.2MB)
테스트 15 〉	통과 (0.49ms, 10.2MB)
테스트 16 〉	통과 (0.53ms, 10.2MB)
테스트 17 〉	통과 (0.64ms, 10.3MB)
테스트 18 〉	통과 (1.47ms, 10.3MB)
테스트 19 〉	통과 (0.65ms, 10.3MB)
테스트 20 〉	통과 (2.08ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (2.84ms, 10.8MB)
테스트 2 〉	통과 (3.02ms, 10.8MB)
테스트 3 〉	통과 (97.35ms, 30.6MB)
테스트 4 〉	통과 (93.80ms, 28.1MB)
'''
def solution(phone_book):
    
    phone_book.sort()
        
    for i in range(1, len(phone_book)):
        
        large_num = phone_book[i]
        small_num = phone_book[i - 1]

        if small_num == large_num[:len(small_num)]:
            return False
                
    return True
'''
정확성  테스트
테스트 1 〉	통과 (0.12ms, 10.2MB)
테스트 2 〉	통과 (0.12ms, 10.3MB)
테스트 3 〉	통과 (0.15ms, 10.2MB)
테스트 4 〉	통과 (0.13ms, 10.3MB)
테스트 5 〉	통과 (0.13ms, 10.3MB)
테스트 6 〉	통과 (0.13ms, 10.2MB)
테스트 7 〉	통과 (0.12ms, 10.2MB)
테스트 8 〉	통과 (0.13ms, 10.3MB)
테스트 9 〉	통과 (0.13ms, 10.2MB)
테스트 10 〉	통과 (0.13ms, 10.2MB)
테스트 11 〉	통과 (0.13ms, 10.3MB)
테스트 12 〉	통과 (0.15ms, 10.3MB)
테스트 13 〉	통과 (0.13ms, 10.2MB)
테스트 14 〉	통과 (0.13ms, 10.3MB)
테스트 15 〉	통과 (0.13ms, 10.2MB)
테스트 16 〉	통과 (0.13ms, 10.2MB)
테스트 17 〉	통과 (0.15ms, 10.2MB)
테스트 18 〉	통과 (0.16ms, 10.4MB)
테스트 19 〉	통과 (0.19ms, 10.2MB)
테스트 20 〉	통과 (0.23ms, 10.3MB)
테스트 21 〉	통과 (0.20ms, 10.2MB)
테스트 22 〉	통과 (0.23ms, 10.3MB)
테스트 23 〉	통과 (0.13ms, 10.2MB)
테스트 24 〉	통과 (0.14ms, 10.3MB)
테스트 25 〉	통과 (0.15ms, 10.3MB)
테스트 26 〉	통과 (0.13ms, 10.4MB)
'''
import re

def solution(new_id):
    # print('#0', new_id)
    
    new_id = new_id.lower()
    # print('#1', new_id)
    
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    # print('#2', new_id)
    
    new_id = re.sub(r'[.]+', '.', new_id)
    # print('#3', new_id)
    
    new_id = new_id.strip('.')
    # print('#4', new_id)
    
    if not new_id:
        new_id = 'a'
    # print('#5', new_id)
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.strip('.')
    # print('#6', new_id)
    
    if 2 >= len(new_id):
        while True:
            new_id += new_id[-1]
            if len(new_id) == 3:
                break
    # print('#7', new_id)
    return new_id
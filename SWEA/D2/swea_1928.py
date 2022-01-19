T = int(input())

def solution(sentence):
    result = ''
    bit_pattern = ''
    base64 = {}
    idx = 0
    
    for alp in range(ord('A'), ord('Z') + 1):
        base64.update({chr(alp): idx})
        idx += 1
        
    for alp in range(ord('a'), ord('z') + 1):
        base64.update({chr(alp): idx})
        idx += 1
        
    for num in range(10):
        base64.update({str(num): idx})
        idx += 1
        
    base64.update({'+': idx})
    base64.update({'/': idx+1})

    for alp in sentence:
        bit_pattern += bin(base64[alp])[2:].zfill(6)
    
    for term in range(0, len(bit_pattern), 8):
        alp = int('0b' + bit_pattern[term:term+8], 2)
        result += chr(alp)
    
    return result

for t in range(1, T + 1):
    answer = solution(input())
    print(f'#{t} {answer}')
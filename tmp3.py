from math import factorial


def solution(width, height, diagonals):
    answer = 0
    for diagonal in diagonals:
        
        
        ar, ac = diagonal[0]-1, diagonal[1] 
        br, bc = diagonal[0], diagonal[1]-1


        center = (factorial(br + bc) // (factorial(br) * factorial(bc))) % 10000019
        goal = (factorial(width + height - br - bc) // (factorial(width - ar) * factorial(height - ac))) % 10000019
        answer += center * goal
        
        center = (factorial(ar + ac) // (factorial(ar) * factorial(ac))) % 10000019
        goal = (factorial(width + height - ar - ac) // (factorial(width - ar) * factorial(height - ac))) % 10000019
        answer += center * goal
    print(answer)
    return answer % 10000019


solution(2, 2, [[1, 1], [2, 2]])
solution(51, 37, [[17, 19]])


import math

def solution2(width, height, diagonals):
    answer = 0
    for diagonal in diagonals:
        r, c = diagonal

        center = (math.factorial(r + c - 1) // (math.factorial(r - 1) * math.factorial(c))) % 10000019
        goal = (math.factorial(width + height - r - c + 1) // (math.factorial(width - r) * math.factorial(height - c + 1))) % 10000019
        answer += center * goal

        center = (math.factorial(r + c - 1) // (math.factorial(r) * math.factorial(c - 1))) % 10000019
        goal = (math.factorial(width + height - r - c + 1) // (math.factorial(width - r + 1) * math.factorial(height - c))) % 10000019
        answer += center * goal
    print(answer)
    return answer % 10000019

solution(2, 2, [[1, 1], [2, 2]])
solution2(51, 37, [[17, 19]])
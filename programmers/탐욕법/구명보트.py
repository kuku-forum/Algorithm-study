from collections import deque

# def solution(people, limit):
#     answer = 0
#     people.sort()
#     i, j = 0, len(people) - 1
    
#     while i <= j:
#         answer += 1 
#         if people[i] + people[j] <= limit:
#             i +=1
#         j -= 1
    
#     return answer

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while people:
        
        if  people[0] + people[-1]  <= limit:
            people.popleft()

        people.pop()
        answer += 1
        
        if len(people) == 1:
            people.pop()
            answer += 1
    
    return answer
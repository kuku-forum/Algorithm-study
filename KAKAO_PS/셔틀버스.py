
'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.03ms, 10.5MB)
테스트 3 〉	통과 (0.02ms, 10.5MB)
테스트 4 〉	통과 (0.03ms, 10.5MB)
테스트 5 〉	통과 (0.04ms, 10.5MB)
테스트 6 〉	통과 (0.03ms, 10.5MB)
테스트 7 〉	통과 (0.73ms, 10.5MB)
테스트 8 〉	통과 (0.02ms, 10.5MB)
테스트 9 〉	통과 (0.03ms, 10.5MB)
테스트 10 〉	통과 (0.03ms, 10.5MB)
테스트 11 〉	통과 (0.09ms, 10.5MB)
테스트 12 〉	통과 (0.30ms, 10.5MB)
테스트 13 〉	통과 (0.51ms, 10.5MB)
테스트 14 〉	통과 (0.20ms, 10.5MB)
테스트 15 〉	통과 (0.13ms, 10.5MB)
테스트 16 〉	통과 (0.33ms, 10.5MB)
테스트 17 〉	통과 (0.58ms, 10.5MB)
테스트 18 〉	통과 (0.28ms, 10.6MB)
테스트 19 〉	통과 (0.29ms, 10.5MB)
테스트 20 〉	통과 (0.51ms, 10.5MB)
테스트 21 〉	통과 (0.95ms, 10.6MB)
테스트 22 〉	통과 (0.35ms, 10.6MB)
테스트 23 〉	통과 (0.37ms, 10.5MB)
테스트 24 〉	통과 (0.87ms, 10.5MB)
'''

def time_convert(arr):
    tmp = []
    for a in arr:
        hour, minute = a.split(':')
        tmp.append(int(hour)*60 + int(minute))
    
    tmp.sort(reverse=True)
    return tmp
    
def solution(n, t, m, timetable):
    answer = ''
    timetable = time_convert(timetable)
    start_init = 540
    line_lst = [[] for _ in range(n)]
    
    for i in range(n):
        start = start_init + i*t
        brk_cnt = 0
        
        while timetable:
            if len(line_lst[i]) == m:
                # print('#1', line_lst[i])
                break
                
            if brk_cnt == m:
                break
                
            if start >= timetable[-1]:
                line_lst[i].append(timetable.pop())
            # print(timetable, brk_cnt)
            brk_cnt += 1
            
    # print(start, line_lst)
    if m > len(line_lst[-1]):
        answer = start
    elif m == len(line_lst[-1]):
        answer = line_lst[-1][-1] - 1
    
    hour, minute = divmod(answer, 60)
    hour, minute = str(hour), str(minute)
    
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    return hour + ':' + minute
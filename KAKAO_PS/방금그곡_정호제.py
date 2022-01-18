import re

def change_melody(txt):
    txt = re.sub('C#', 'V', txt)
    txt = re.sub('D#', 'W', txt)
    txt = re.sub('F#', 'X', txt)
    txt = re.sub('G#', 'Y', txt)
    txt = re.sub('A#', 'Z', txt)
    return txt

def change_time(txt):
    txt_lst = txt.split(':')
    return int(txt_lst[0])*60 + int(txt_lst[1])

def change_len(time, txt):
    q, r = divmod(time, len(txt))
    return txt*q + txt[:r] if q > 0 else txt[:r]
    
def solution(m, musicinfos):
    answer = []
    target = change_melody(m)
    
    for info in musicinfos:
        info_lst = info.split(',')
        time = change_time(info_lst[1]) - change_time(info_lst[0])
        melody = change_len(time, change_melody(info_lst[3]))
        
        if target in melody:
            answer.append([info_lst[2], time])

    return max(answer, key = lambda x: x[1])[0] if answer else "(None)"

'''
정확성  테스트
테스트 1 〉	통과 (0.18ms, 10.5MB)
테스트 2 〉	통과 (0.18ms, 10.4MB)
테스트 3 〉	통과 (0.27ms, 10.4MB)
테스트 4 〉	통과 (0.17ms, 10.3MB)
테스트 5 〉	통과 (0.17ms, 10.4MB)
테스트 6 〉	통과 (0.19ms, 10.3MB)
테스트 7 〉	통과 (0.28ms, 10.5MB)
테스트 8 〉	통과 (0.28ms, 10.3MB)
테스트 9 〉	통과 (0.27ms, 10.4MB)
테스트 10 〉	통과 (0.27ms, 10.3MB)
테스트 11 〉	통과 (0.28ms, 10.2MB)
테스트 12 〉	통과 (0.26ms, 10.2MB)
테스트 13 〉	통과 (0.28ms, 10.5MB)
테스트 14 〉	통과 (0.28ms, 10.4MB)
테스트 15 〉	통과 (0.27ms, 10.3MB)
테스트 16 〉	통과 (0.28ms, 10.3MB)
테스트 17 〉	통과 (0.26ms, 10.3MB)
테스트 18 〉	통과 (0.26ms, 10.4MB)
테스트 19 〉	통과 (0.32ms, 10.4MB)
테스트 20 〉	통과 (0.27ms, 10.3MB)
테스트 21 〉	통과 (0.28ms, 10.5MB)
테스트 22 〉	통과 (0.28ms, 10.3MB)
테스트 23 〉	통과 (0.26ms, 10.4MB)
테스트 24 〉	통과 (0.27ms, 10.5MB)
테스트 25 〉	통과 (0.18ms, 10.3MB)
테스트 26 〉	통과 (0.20ms, 10.4MB)
테스트 27 〉	통과 (0.19ms, 10.4MB)
테스트 28 〉	통과 (0.18ms, 10.4MB)
테스트 29 〉	통과 (1.96ms, 10.4MB)
테스트 30 〉	통과 (1.76ms, 10.4MB)
'''
import re
from datetime import datetime, timedelta

def solution(m, musicinfos):
    m = re.sub('C#', 'c', m)
    m = re.sub('D#', 'd', m)
    m = re.sub('F#', 'f', m)
    m = re.sub('G#', 'g', m)
    m = re.sub('A#', 'a', m)
    
    # timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    answer = []
    
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(',')
        
        info = re.sub('C#', 'c', info)
        info = re.sub('D#', 'd', info)
        info = re.sub('F#', 'f', info)
        info = re.sub('G#', 'g', info)
        info = re.sub('A#', 'a', info)
        
        SH, SM = map(int, start.split(':'))
        EH, EM = map(int, end.split(':'))
        d1 = datetime(year= 2020, month=1, day =15, hour=SH, minute=SM)
        d2 = datetime(year= 2020, month=1, day =15, hour=EH, minute=EM)
        dm = (d2 - d1).seconds//60
        
        q, r = divmod(dm, len(info))
        info = info*q + info[:r]
        
        if m in info:
            answer.append([title, dm])
        
    if len(answer) == 0:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][0]
    else:
        answer.sort(key = lambda x: -x[1])
        return answer[0][0]
    

from my_package.hjtc import swea_tc

for t in range(1, int(input()) + 1):
    answer = 0
    N = int(input())
    timeline_lst = [list(map(int, input().split())) for _ in range(N)]
    timeline_lst.sort(key=lambda x: -x[1])
    schedule = [0 for _ in range(25)]
    
    for end_time in range(1, 25):
        
        if timeline_lst and timeline_lst[-1][1] == end_time:
            while timeline_lst and timeline_lst[-1][1] == end_time:
                schedule[end_time] = max(schedule[timeline_lst[-1][0]] + 1, schedule[end_time-1], schedule[end_time])
                timeline_lst.pop()
        else:
            schedule[end_time] = schedule[end_time-1]
        
    print(f'#{t} {schedule[-1]}')
            
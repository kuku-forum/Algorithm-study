def battle(num1, num2):
    if num1[1] == 1 and num2[1] == 2:
        return num2
    
    elif num1[1] == 1 and num2[1] == 3:
        return num1
    
    elif num1[1] == 2 and num2[1] == 1:
        return num1
    
    elif num1[1] == 2 and num2[1] == 3:
        return num2
    
    elif num1[1] == 3 and num2[1] == 1:
        return num2
    
    elif num1[1] == 3 and num2[1] == 2:
        return num1
    
    else:
        if num1[0] > num2[0]:
            return num2
        else:
            return num1
        

def tournament(arr):
    # 2개만 남았을 경우 가위바위보 해서 하나 반환
    if len(arr) == 2:
        return battle(arr[0], arr[1])
    
    # 1개 남았을경우 원소만 반환
    if len(arr) == 1:
        return arr[0]
    
    # 절반으로 나눔
    pivot = len(arr)//2
    if len(arr)%2 == 1:
        lesser_arr = arr[:pivot + 1]
        greater_arr = arr[pivot + 1:]
    else:
        lesser_arr = arr[:pivot]
        greater_arr = arr[pivot:]
        
    
    return battle(tournament(lesser_arr), tournament(greater_arr))   


for t in range(1, int(input()) + 1):
    N = int(input())
    arr = []
    for i, num in enumerate(map(int, input().split())):
        arr.append([i+1, num ])
    
    answer = tournament(arr)
    print(f'#{t} {answer[0]}')
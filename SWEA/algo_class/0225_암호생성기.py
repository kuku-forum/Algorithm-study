from my_package.hjtc import swea_tc as print


def solution(arr):
    
    while True:
        for i in range(1, 6):
            num = arr.pop(0) - i
            
            if 0 >= num:
                num = 0
                
            arr.append(num)
            
            if arr[-1] == 0:
              return arr
    
    
for t in range(1, 11):
    _ = input()
    arr = list(map(int, input().split()))

    print(f'#{t} {" ".join(map(str, solution(arr)))}')
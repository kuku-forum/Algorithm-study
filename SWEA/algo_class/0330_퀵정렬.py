from my_package.hjtc import swea_tc

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left, mid, right = [], [], []
    
    for n in arr:
        if pivot > n:
            left.append(n)
        elif pivot < n:
            right.append(n)
        else:
            mid.append(n)
    
    return quicksort(left) + mid + quicksort(right)

def timsort(arr):
    return sorted(arr)

def mergesort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    
    # 절반으로 계속 나눈다
    mid = len(arr)//2
    left_arr = mergesort(arr[:mid])
    right_arr = mergesort(arr[mid:])
    
    # 병합할 리스트
    merged_arr = []
    l = r = 0
    
    # 문제 조건
    if left_arr[-1] > right_arr[-1]:
        cnt += 1
    
    # 0부터 인덱스 범위까지, 좌/우 두 리스트중 작은 원소를 merged_arr에 담는다
    while len(right_arr) > r and len(left_arr) > l:
        if right_arr[r] > left_arr[l]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])
            r += 1
            
    # 남아있는 원소들을 merged_arr에 추가
    merged_arr += left_arr[l:]
    merged_arr += right_arr[r:]
    return merged_arr

for t in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    n_lst = list(map(int, input().split()))
    sorted_arr = mergesort(n_lst)
    
    print(f'#{t} {sorted_arr[N//2]} {cnt}')
N = int(input())
arr = list(map(int, input().split()))

fowd = [1]
back = [1]

for i in range(1, len(arr)):
    if arr[i] >= arr[i - 1]:
        fowd.append(fowd[i - 1] + 1)
    else:
        fowd.append(1)
        

for i, j in enumerate(range(len(arr) - 2, -1, -1)):
    if arr[j] >= arr[j + 1]:
        back.append(back[i ] + 1)
    else:
        back.append(1)
    
print(max(max(fowd), max(back)))
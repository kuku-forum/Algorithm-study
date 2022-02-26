N = int(input())
arr = []

dasom = int(input())
for _ in range(N - 1):
    arr.append(int(input()))
    
    
answer = 0
arr.sort()

while arr and arr[-1] >= dasom :
    dasom += 1
    arr[-1] -= 1
    answer += 1
    arr.sort()
    
print(answer)
N = int(input())
answer = []

for num in range(N, -1, -1):
    answer.append(num)
    
print(' '.join(map(str, answer)))
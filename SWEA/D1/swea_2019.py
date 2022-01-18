N = int(input())

answer = []

for power in range(N + 1):
    answer.append(2**power)
    
print(' '.join(map(str, answer)))
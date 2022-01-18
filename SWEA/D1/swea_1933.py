N = int(input())
answer = []
for i in range(1, int(N**0.5)+1):
    if N%i == 0:
        answer.append(i)
        answer.append(N//i)
        
answer.sort()
print(' '.join(map(str, answer)))
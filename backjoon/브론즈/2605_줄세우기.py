N = int(input())

answer = []

for student, idx in enumerate(map(int, input().split())):
    answer.insert(student - idx, student + 1)
    
print(' '.join(map(str, answer)))
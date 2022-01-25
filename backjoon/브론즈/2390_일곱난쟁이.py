from itertools import combinations

person_list = []

for _ in range(9):
    person_list.append(int(input()))
    
for arr in combinations(person_list, 7):
    if sum(arr) == 100:
        for num in sorted(arr):
            print(num)
        break


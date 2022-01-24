# num_map_list 와 num_list의 size 차이 이유?
# 리스트 각 원소의 사이즈 합은 172인데 왜 전체 list의 사이즈는 이보다 작은 160, 112인가?

import sys

num_str = '0 2 3 81 3447 9599999999999999998'
num_list = [0, 2, 3, 81, 3447, 9599999999999999998]
num_map_list = list(map(int, num_str.split()))

print()
print('num_str: ', sys.getsizeof(num_str)) # 82
# print(len(num_str), len(num_str)*4)
print('list(map()) 함수를 사용한 num_list, using getsizeof: ', sys.getsizeof(num_map_list)) # 160
print('list(map()) 함수를 사용한 num_list, using sizeof: ', num_map_list.__sizeof__(), id(num_map_list)) # 126
print('num_list, using getsizeof: ', sys.getsizeof(num_list)) # 112
print('num_list, using sizeof : ', num_list.__sizeof__()) # 88

# print()
# print('num_list 존재하는 숫자(int) 마다의 크기')
# int_size_total = 0
# for num in num_list:
#     num_size = sys.getsizeof(num)
#     int_size_total += num_size
#     print(f'int {num}: ', num_size)
    

# print(f'int size_total: ', int_size_total) # 172


print()
print('num_list 존재하는 숫자(int) 마다의 크기, getsizeof가 아닌 __sizeof__() 사용')
list_size_total = 0
list_idx_size_total = 0
for i, num in enumerate(num_list):
    num_size = num.__sizeof__()
    list_size_total += num_size
    list_idx_size_total += num_list[i].__sizeof__()
    print(f'int {num}: ', num_size, num_list[i].__sizeof__(), id(num_size).__sizeof__())
    
print(f'int size_total: {list_size_total}')
print(f'list_idx_size_total: {list_idx_size_total}', )



''' 
num_str:  82
list(map()) 함수를 사용한 num_list:  160
list(map()) 함수를 사용한 num_list:  136
num_list:  112
num_list:  88

num_list 존재하는 숫자(int) 마다의 크기
int 0:  24
int 2:  28
int 3:  28
int 81:  28
int 3447:  28
int 9599999999999999998:  36
int size_total:  172

num_list 존재하는 숫자(int) 마다의 크기, getsizeof가 아닌 __sizeof__() 사용
int 0:  24
int 2:  28
int 3:  28
int 81:  28
int 3447:  28
int 9599999999999999998:  36
int size_total:  172
'''

'''
getsizeof vs __sizeof__()

Note:The sys.getsizeof() function includes the marginal space usage, 
which includes the garbage collection overhead for the object. 
Meaning it returns the total space occupied by the object in addition to the garbage collection overhead for the spaces being used.

1.Using inbuilt __sizeof__() method:

Python also has an inbuilt __sizeof__() method to determine the space allocation of an object without any additional garbage value. 
It has been implemented in the below example.

# https://www.geeksforgeeks.org/find-the-size-of-a-list-python/
'''
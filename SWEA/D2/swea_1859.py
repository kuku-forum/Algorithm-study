import sys

num_str = '0 2 3 81 3447 9599999999999999998'
num_list = [0, 2, 3, 81, 3447, 9599999999999999998]
num_map_list = list(map(int, num_str.split()))

print()
print('num_str: ', sys.getsizeof(num_str)) # 82
# print(len(num_str), len(num_str)*4)
print('list(map()) 함수를 사용한 num_list: ', sys.getsizeof(num_map_list)) # 160
print('num_list: ', sys.getsizeof(num_list)) # 112

print()
print('각 숫자(int) 마다의 크기')
int_size_total = 0
for num in num_list:
    num_size = sys.getsizeof(num)
    int_size_total += num_size
    print(f'int {num}: ', num_size)
    
print(f'int size_total: ', int_size_total) # 172


print()
print('num_list 존재하는 숫자(int) 마다의 크기')
list_size_total = 0
for num in num_map_list:
    num_size = sys.getsizeof(num)
    list_size_total += num_size
    print(f'int {num}: ', num_size)
    
print(f'int size_total: ', list_size_total)

# num_map_list 와 num_list의 size 차이 이유?
# 리스트 각 원소의 사이즈 합은 172인데 왜 전체 list의 사이즈는 이보다 작은 160, 112인가?
''' 
num_str:  82
list(map()) 함수를 사용한 num_list:  160
num_list:  112

각 숫자(int) 마다의 크기
int 0:  24
int 2:  28
int 3:  28
int 81:  28
int 3447:  28
int 9599999999999999998:  36
int size_total:  172

num_list 존재하는 숫자(int) 마다의 크기
int 0:  24
int 2:  28
int 3:  28
int 81:  28
int 3447:  28
int 9599999999999999998:  36
int size_total:  172
'''
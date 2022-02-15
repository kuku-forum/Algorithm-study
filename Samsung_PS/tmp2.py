def gen_combi(arr, n):
    result = []
    if n == 0:
        return [[]]

    for i in range(0, len(arr)):
        elem = arr[i]
        for C in gen_combi(arr[i + 1:], n - 1):
            result.append([elem] + C)
    print(result)       
    return result


a = [1,2,3]
print(gen_combi(a, 10))
# []

# a = [1] + []

# print(a)
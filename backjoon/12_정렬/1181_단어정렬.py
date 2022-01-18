import sys

N = int(sys.stdin.readline())

word_list = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    word_list.append((word, len(word)))

word_list = list(set(word_list))
word_list.sort(key = lambda word: (word[1], word[0]))

for word in word_list:
    print(word[0])


# word_dict_sorted = sorted(word_dict.items(), key = lambda item: item[1])
# # print(word_dict_sorted, type(word_dict_sorted), type(word_dict_sorted[0]))

# for i in range(len(word_dict_sorted)):
#     tmp = []
#     if i == len(word_dict_sorted)-1:
#         word_list.append(word_dict_sorted[i][0])

#     if word_dict_sorted[i][0] in word_list:
#         continue

#     for j in range(i+1, len(word_dict_sorted)):

#         if word_dict_sorted[i][1] != word_dict_sorted[j][1]:
#             if len(tmp) == 0:
#                 word_list.append(word_dict_sorted[i][0])
#                 break
#             else:
#                 tmp.append(word_dict_sorted[i][0])
#                 for word in sorted(tmp):
#                     word_list.append(word)
#                 break
#         else:
#             # print(word_dict_sorted[j][0])
#             tmp.append(word_dict_sorted[j][0]) 

# for word in word_list:
#     print(word)         


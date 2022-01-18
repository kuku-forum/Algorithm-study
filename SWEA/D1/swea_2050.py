alp_lst = input()

alp_dic = {chr(alp): num+1 for num, alp in enumerate(range(ord('A'), ord('Z') + 1))}
num_lst = [alp_dic[alp] for alp in alp_lst]

print(' '.join(map(str, num_lst)))
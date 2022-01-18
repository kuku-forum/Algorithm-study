def black_jack():
    
    global M, nums
    sample_abs_val = M[1]
    num_len = M[0]
    target_num = M[1]
    sample_trigger = True
    
    for i in range(0, num_len-2):
        for j in range(i+1, num_len-1):
            for k in range(j+1, num_len):
                
                tmp_val = nums[i] + nums[j] + nums[k]
                sub_val = target_num - tmp_val
                
                if sub_val == 0: 
                    return tmp_val
                
                if target_num >= tmp_val and sample_trigger:
                    sample_abs_val = sub_val
                    sample_trigger = False
                
                if sample_abs_val > sub_val >= 0 and sample_trigger == False:
                    sample_abs_val = sub_val
                    answer = tmp_val
    return answer
            
M = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]

result = black_jack()
print(result)
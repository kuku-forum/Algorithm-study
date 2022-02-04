'''
  A 
B C D E
  F 
'''

N = int(input())

dice_list = []
for _ in range(N):
    dice_list.append(list(map(int, input().split())))
    

def dice_rot(arr, idx):
    
    if idx == 2:
        return arr
    
    elif idx == 1:
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[4], arr[1], arr[2], arr[3], arr[5]
        return arr
    
    elif idx == 3:
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[2], arr[3], arr[4], arr[1], arr[5]
        return arr
        
    elif idx == 4:
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[3], arr[4], arr[1], arr[2], arr[5]
        return arr
        
    elif idx == 5:
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[2], arr[1], arr[5], arr[3], arr[0], arr[4]
        return arr
        
    elif idx == 0:
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[4], arr[1], arr[0], arr[3], arr[5], arr[2]
        return arr
    
def dice_re_rot(arr, idx):
    
    if idx == 2:
        return arr
    
    elif idx == 1:
        arr[0], arr[4], arr[1], arr[2], arr[3], arr[5] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] 
        return arr
    
    elif idx == 3:
        arr[0], arr[2], arr[3], arr[4], arr[1], arr[5] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
        return arr
        
    elif idx == 4:
        arr[0], arr[3], arr[4], arr[1], arr[2], arr[5] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
        return arr
        
    elif idx == 5:
        arr[2], arr[1], arr[5], arr[3], arr[0], arr[4] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
        return arr
        
    elif idx == 0:
        arr[4], arr[1], arr[0], arr[3], arr[5], arr[2] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
        return arr
    
answer = 0

for i in range(6):
    tmp = 0
    dice_1 = dice_rot(dice_list[0], i)
    top_val = dice_1[4]
    tmp += max(dice_1[0], dice_1[1], dice_1[3], dice_1[5])
    dice_1 = dice_re_rot(dice_list[0], i)
    
    for floor in range(1, N):
        bottom_val = dice_list[floor].index(top_val)
        up_dice = dice_rot(dice_list[floor], bottom_val)
        top_val = up_dice[4]
        tmp += max(up_dice[0], up_dice[1], up_dice[3], up_dice[5])
        up_dice = dice_re_rot(dice_list[floor], bottom_val)
    
    answer = max(answer, tmp)
    
print(answer)
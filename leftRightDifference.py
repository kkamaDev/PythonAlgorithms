def LeftRightDiffirence(nums:list)->list:
    left,right  = 0 , sum(nums) 
    result = []
    for num in nums:
        left+=num
        
        if right - left > 0:
            result.append(1)
        elif right - left < 0:
            result.append(-1)
        else:
            result.append(0)
        right-=num
    return result
print(LeftRightDiffirence([1,2,3,4]))


# yoki bo'lmasa kodni chiroyliroq qilish uchun sign deb alohida funksiya bilan tekshirish mumkin

# def sign(num):
#     if num  > 0:
#         return 1
#     elif num < 0:
#         return -1
#     return 0 
    
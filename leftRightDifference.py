def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    return 0



def LeftRightDiffirence(nums:list)->list:
    left,right  = 0 , sum(nums) 
    result = []
    for num in nums:
        left+=num
        result.append(sign(right-left))
        
        right-=num
    return result
print(LeftRightDiffirence([1,2,3,3]))
    
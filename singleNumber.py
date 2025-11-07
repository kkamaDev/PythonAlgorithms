def SingleNum(nums:list):
    result = 0
    for num in nums:
        result = result ^ num
    
    return result
print(SingleNum([1,1,2,3,3]))
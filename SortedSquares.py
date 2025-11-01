def SortedSquares(nums:list)->list:
    i , j = 0 , len(nums) -1
    result = []
    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result.append(nums[j]**2)
            j-=1
        else:
            result.append(nums[i]**2)
            i+=1
    result.reverse()
    return result
    
print(SortedSquares([-4,0,2,3]))
        
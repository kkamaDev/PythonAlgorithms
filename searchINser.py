def searchInser(nums:list , target):
    left , right = 0 , len(nums) -1
    while left <=right:
        mid = (left+right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid +1
        else:
            right = mid-1
    return left
sinov = searchInser([1,2,3,5,6] , 7)
print(sinov)
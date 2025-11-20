def twoSum(nums,target): # -- bizga sonlar ro'yxati va target keladi numsdan -- list qaytaradi
    for i in range(len(nums)): # har bir elementni indexini qaytaradi masalan [2,7]-- 0,1 
        for j in range(i+1, len(nums)): # 2 - qo'shiladigan sonimzni indexni qaytaramiz i+1 bu yerda sonni o'zini olmaymiz 
            if nums[i]+ nums[j] == target: # i va j indexdagi sonlarni yig'indisini targetga tengligini tekshiramiz 
                return [i, j] # va shu sonlarni indexni qaytaradi
solution = twoSum([2,7,11,12], 9)
print(solution)
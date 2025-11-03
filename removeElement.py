def removeElement(nums:list,val):
    j = 0  # val ga teng bo'lmagan sonlarni saqlaymiz 
    for i in range(len(nums)):  # ro'yxat boshidan oxirgacha yurib chiqamiz 
        if nums[i] != val: # agar elementimz val ga teng bo'lmasa j ga almashtramiz 
            nums[j] = nums[i] # har safar val ga teng bo'lmasa qo'shib ketadi
            j+=1
    return j
print(removeElement([2,2,3,3], 3))
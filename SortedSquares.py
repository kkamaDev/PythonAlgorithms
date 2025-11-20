def SortedSquares(nums:list)->list:  
    i , j = 0 , len(nums) -1  # boshi va oxirigi qiymatlarni olamiz oxirini olish uchun ro'yxat uzunligini -1 qilsak oxirgi qymatga o'tadi
    result = [] # natijasni saqlash uchun array yaratib olamiz
    while i <= j:  #ikkalasi teng bo'lib qolsa sikl to'xtaydi 
        if abs(nums[i]) < abs(nums[j]): # ro'yxatdagi sonlarni musbat songa o'tqzib solishtramiz abs() sonni musbat ga o'tqazadi
            result.append(nums[j]**2) # j katta holatida uni kvadratini saqlaymiz 
            j-=1 # va oxirgi sonni bitta oldinga suramiz [-4,0,2] bo'ladi
        else:
            result.append(nums[i]**2) # ask holda boshidagi sonni qo'shamiz 
            i+=1 # va bitta oldinga suramiz 
    result.reverse() #[16,9,4,0] bo'ladi bizga esa o'sish tartibda kerak uni reverse( ) qilsak ro'yxatni aylantrb beradi
    return result
    
print(SortedSquares([-4,0,2,3]))
        
def maxArea(nums: list) -> int:
  i , j = 0 , len(nums) -1 # ro'yxatni boshi va oxirini olamiz 
  max_area = 0  # yzuamizni eng kattasini saqlab boramiz va qaytaramiz 
  while i < j:  # index lar  bir briga teng bo'lib qolsa ular yaqinlashib bitta ustunga teng bo'lib qoladi
    area = (j-i) * min(nums[i] , nums[j]) #   (j-i) enini qaytaradi min(nums[i] , nums[j]) eng kichik devor uzunligigacha to'ladi
    max_area = max(area , max_area) # agara area miz katta bo'lsa qiymat yangilab qo'yamiz 
    if nums[i] > nums[j]:  # ustunlarni siljitamiz agar boshidagi qiymatlar katta bo'lsa ro'yxatni oxiridan qsqartramiz 
        j-=1
    else:
        i+=1
  return max_area 

print(maxArea([1,8,6,2,5,4,8,3,7]))


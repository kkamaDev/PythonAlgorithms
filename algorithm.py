# nums = int(input("son kriiting >>"))
# sum = 0
# for num in str(nums):
#     sum = sum + int(num)
# print(sum)


# # sonni max  va min topish
# nums = [1,5,3,7,9,6,4]
# max_s = nums[0]
# min_s = nums[0]
# for i in nums:
#     if i < min_s:
#         min_s = i
#     if i > max_s:
#         max_s = i 
# print(f"min {min_s}")
# print(f"max : {max_s}")






# # nollarni ortga surish

# def moveZero(nums:list):
#     count = 0
#     for i , num in enumerate(nums):
#         if num == 0:
#             count+=1
#             continue
#         nums[i] , nums[i-count] = nums[i-count] , nums[i]
#     return nums
# son = [0,1,2,0,12]
# print(moveZero(son))



def teskari(x):
    teskari = 0
    oxirgi = x % 10
    teskari = teskari * 10 + oxirgi
    x = x // 10
    return x
print(teskari(123))
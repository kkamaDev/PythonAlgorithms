def prod(nums:list):
    prefix = [1]
    suffex = [1]
    
    product = 1
    for num in nums:
        product*= num
        prefix.append(product)
    product = 1
    for num in reversed(nums):
        product*=num
        suffex.append(product)
    suffex.reverse()
    
    result = []
    for i in range(len(nums)):
        prod = prefix[i] * suffex[i+1]
        result.append(prod)
    return result
    
        
    
print(prod([1,2,3,4]))
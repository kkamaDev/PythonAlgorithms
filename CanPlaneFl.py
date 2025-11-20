def CanPlaneFl(flowerbed:list , n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left = ([i==0] or (flowerbed[i-1]==0))
            right = (len(flowerbed) - 1 ==i) or (flowerbed[i+1] ==0)
            
            if right and left:
                flowerbed[i] = 1
                n-=1
                
                if  n ==0:
                    return True 
            return n <=0
    
print(CanPlaneFl([1,0,0,0,0,1] , 4))
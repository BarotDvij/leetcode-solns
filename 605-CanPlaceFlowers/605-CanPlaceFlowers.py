# Last updated: 10/15/2025, 3:03:15 AM
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        check = True  
        i = 1

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1 
                
        else:
            if flowerbed[0] == 0 and flowerbed[1] == 0: 
                flowerbed[0] = 1
                n -= 1

            if flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
                flowerbed[len(flowerbed) - 1] = 1
                n -= 1

            while i < len(flowerbed) - 1 and n > 0:
                if flowerbed[i] == 0:
                    prev = flowerbed[i - 1] == 0
                    nex = flowerbed[i + 1] == 0

                    if prev and nex:
                        flowerbed[i] = 1
                        n -= 1
                i += 1
            
        if n > 0:
            check = False
        
        return check

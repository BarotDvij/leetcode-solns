# Last updated: 10/15/2025, 3:03:22 AM
class Solution(object):
    def increasingTriplet(self, nums):
        one = two = float('inf')
        for i in nums:
            if i < one:
                one = i
            
            if one < i < two:
                two = i

            if two < i:
                return True
        
        return False
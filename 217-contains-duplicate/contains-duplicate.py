class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return False
        
        occurences = {}

        for n in nums:
            if n in occurences:
                return True
            else:
                occurences[n] = 1

        return False

        

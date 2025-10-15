# Last updated: 10/15/2025, 3:03:24 AM
class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
        return nums
 
        
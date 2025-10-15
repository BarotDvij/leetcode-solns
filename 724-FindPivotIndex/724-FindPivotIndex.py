# Last updated: 10/15/2025, 3:03:12 AM
class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0

        totsum = 0
        for a in range(len(nums)):
            totsum += nums[a]

        for i in range(len(nums)):
            right_sum = totsum - left_sum - nums[i]  
            if left_sum == right_sum:
                return i 
            left_sum += nums[i]
        return -1
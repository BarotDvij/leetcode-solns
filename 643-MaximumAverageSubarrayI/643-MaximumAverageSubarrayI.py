# Last updated: 10/15/2025, 3:03:13 AM
class Solution(object):
    def findMaxAverage(self, nums, k):
        ans = sum1 = sum(nums[:k])

        for i in range(len(nums)-k):
            sum1 = sum1 - nums[i] + nums[i+k]
            if sum1 > ans:
                ans = sum1
        
        return ans/float(k) 
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
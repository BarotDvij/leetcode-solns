# Last updated: 10/15/2025, 3:03:09 AM
class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeroes = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            
            # Shrink the window only if we exceed the limit of k zeroes
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1  # Move the left pointer
            
            # Update max length of the window
            max_len = max(max_len, right - left + 1)
        
        return max_len
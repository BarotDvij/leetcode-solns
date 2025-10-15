# Last updated: 10/15/2025, 3:03:01 AM
class Solution(object):
    def longestSubarray(self, nums):
        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):
            # If we encounter a zero, increase the zero count
            if nums[right] == 0:
                zero_count += 1

            # If we have more than one zero, shrink the window from the left
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the maximum length - we subtract 1 to account for one deletion
            max_length = max(max_length, right - left)

        return max_length

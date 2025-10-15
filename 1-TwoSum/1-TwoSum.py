# Last updated: 10/15/2025, 3:07:38 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {} #makes dictionary
        for i in range(len(nums)):
            if (target - nums[i]) in array:
                return [array[target - nums[i]], i]
            array[nums[i]] = i
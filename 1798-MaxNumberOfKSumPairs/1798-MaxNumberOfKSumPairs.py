# Last updated: 10/15/2025, 3:02:59 AM
class Solution(object):
    def maxOperations(self, nums, k):
        #reduces the length of unnecessary nums
        nums = [n for n in nums if n < k]
       
        #this allows us to move the left and right pointer depending
        #on the condition of the pair sums
        nums.sort()

        #declare variables in a sexy way
        i, j, c = 0, len(nums)-1, 0

        #loop that determines the number of pairs with the "c" counter variable
        while i < j:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                i += 1
                j -= 1
                c += 1

        return c
# Last updated: 10/15/2025, 3:03:24 AM
class Solution(object):
    def productExceptSelf(self, nums):
        l = r = 1
        lp= []
        rp= []
        ans=[]

        for i in range(len(nums)):
            r *= nums[i]
            rp.append(r)
            ans.append(1)

        for j in range(len(nums) - 1, -1, -1):
            l *= nums[j]
            lp.append(l)
            ans[j] = rp[j-1] * lp[len(nums)-2-j]
            
        ans[len(nums)-1] = rp[len(nums)-2]
        ans[0] = lp[len(nums)-2]
        
        return ans
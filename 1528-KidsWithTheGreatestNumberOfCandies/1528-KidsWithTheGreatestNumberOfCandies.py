# Last updated: 10/15/2025, 3:03:03 AM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = [False] * len(candies)

        for i in range(len(candies)):
            candies[i] += extraCandies
            if max(candies) == candies[i]:
                ans[i] = True
            candies[i]-= extraCandies
        
        return ans
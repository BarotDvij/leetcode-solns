# Last updated: 10/15/2025, 3:03:25 AM
class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        ans = ""
        for i in range(len(words)):
            ans += words[(len(words)-1)-i] + " "
        return ans[:-1] 
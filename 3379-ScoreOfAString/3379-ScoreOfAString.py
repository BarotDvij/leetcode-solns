# Last updated: 10/15/2025, 3:02:52 AM
class Solution(object):
    def scoreOfString(self, s):
        ans = 0
        for i in range(0, len(s)-1, 1):
            diff = abs(ord(s[i]) - ord(s[i+1]))
            ans += diff
        return ans
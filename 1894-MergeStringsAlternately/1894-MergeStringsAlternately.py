# Last updated: 10/15/2025, 3:02:57 AM
class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans = ""
        for i in range(min(len(word1), len(word2))):
            ans += word1[i] + word2[i]

        ans += word1[i+1:] + word2[i+1:]
            
        return ans
        
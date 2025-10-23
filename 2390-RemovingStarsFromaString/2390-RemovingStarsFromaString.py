# Last updated: 10/23/2025, 12:05:07 AM
class Solution:
    def removeStars(self, s: str) -> str:
        starless = ''
        for i in range(len(s)):
            starless += s[i]
            if s[i] == '*':
                starless = starless[:-1]
                starless = starless[:-1]
        return starless
        
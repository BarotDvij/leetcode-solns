# Last updated: 10/23/2025, 12:30:41 AM
class Solution:
    def removeStars(self, s: str) -> str:
        starless = []
        for i in range(len(s)):
            starless.append(s[i])
            if s[i] == '*':
                starless.pop()
                starless.pop()
        return ''.join(starless)
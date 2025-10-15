# Last updated: 10/15/2025, 3:03:21 AM
class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0 

        
        if len(s) > len(t): return False

        if s == "" or s == t: return True
        
        elif len(t) > len(s):
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                if i >= len(s):
                    return True
                j += 1
        
        return False


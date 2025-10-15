# Last updated: 10/15/2025, 3:03:09 AM
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        shorter = str1 if len(str1) <= len(str2) else str2
        longer = str1 if len(str1) > len(str2) else str2
        ans = shorter

        if longer + shorter == shorter + longer:
            for i in range(len(shorter)-1, 0, -1):
                if len(shorter) % len(ans) == 0 and len(longer) % len(ans) == 0:
                    return ans
                ans = ans[:-1]
                print ans
        else:
            ans = ""
        
        return ans
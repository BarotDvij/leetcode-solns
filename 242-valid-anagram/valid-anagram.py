'''
iterate over t to see if it has the same count of letters as
in s.

**Q: Can we count s AND t at the same time to see if they match
instead of building a hash map for s with counts as its values?

New Idea: what if s was +ve values, t was -ve values, and then if the
values for each key came out to 0, it is an anagram?"
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #initial check
        #avoids needing to iterate over map w/all function to check if the vals are 0
        if len(s) != len(t):
            return False 
        
        #hash map
        counts = {}
        
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        for c in t:
            if c in counts:
                counts[c] -= 1
                if counts[c] < 0:
                    return False
            else:
                return False
        
        return True
# Last updated: 10/15/2025, 3:03:03 AM
class Solution(object):
    def maxVowels(self, s, k):
        vowels = {"a","e","i","o","u"}
        st = list(s)
        count = 0
        
        for a in st[:k]:
            if a in vowels:
                count +=1
        high = count
      
        for i in range(len(st)-k):
            if st[i] in vowels:
                count -= 1
            
            if st[k+i] in vowels:
                count += 1

            if count > high:
                high = count
            
            if high == k:
                return k
        
        return high
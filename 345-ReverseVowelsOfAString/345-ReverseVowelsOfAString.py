# Last updated: 10/15/2025, 3:03:21 AM
class Solution(object):
    def reverseVowels(self, s): 
        vowels = {'A','a','E','e','I','i','O','o','U','u'}
        st = list(s)
        index = []
    
        for i in range(len(st)):
            if st[i] in vowels:
                index.append(i)
        
        for j in range(len(index)//2):
            st[index[j]], st[index[-(j + 1)]] = st[index[-(j + 1)]], st[index[j]]
        

        return ''.join(st)

        

        
        
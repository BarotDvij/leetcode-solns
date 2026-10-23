class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        '''
        cannot be sliding window since one end is tied to position
        0 (since it's a prefix)
        '''
        #If there's only 1 item, aka 1 word, in the array
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0] 
        '''
        IF ALL OF THE LOOPS PASSED THEN NO LETTER AKA Column FAILED, which means we must return the full 1st word
        '''

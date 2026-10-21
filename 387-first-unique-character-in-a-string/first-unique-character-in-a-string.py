class Solution:
    def firstUniqChar(self, s: str) -> int: 
        letters = {}

        #loops over dict to mark repeated letters
        for i, char in enumerate(s):
            if char in letters:
                letters[char] = -1
            else: 
                letters[char] = i

        #returns 1st value > -1
        for char in letters:
            if letters[char] > -1:
                return letters[char]

        return -1
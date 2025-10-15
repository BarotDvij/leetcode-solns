# Last updated: 10/15/2025, 3:03:00 AM
class Solution(object):
    def closeStrings(self, word1, word2):
        #to clear simple outlier cases quicker
        if len(word1) != len(word2) or set(word1) != set(word2): return False
        
        #OP 1- checking indices to find just one missing
        swap = 0 
        for j in range(len(word1)):
            if word1[j] != word2[j]: swap += 1
        if swap < 2: return True

        #OP 2- checking frequency and indices to find switchable character
        dick1, dick2 = {}, {}
        for c in range(len(word1)):
            if word1[c] not in dick1: dick1[word1[c]] = 1
            else: dick1[word1[c]] += 1

            if word2[c] not in dick2: dick2[word2[c]] = 1
            else: dick2[word2[c]] += 1
        #checks to see if the values, so frequency, of the characters line up
        #(i.e. are there enough a's to match the b's)
        if sorted(dick1.values()) == sorted(dick2.values()): return True

        return False
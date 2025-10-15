# Last updated: 10/15/2025, 3:02:53 AM
class Solution(object):
    def removeStars(self, s):
        stack = []
        
        for i in s: 
            if i !=  "*": stack.append(i)
            else: stack.pop()
        
        return ''.join(stack)

        """
        :type s: stackr
        :rtype: stackr
        """
        
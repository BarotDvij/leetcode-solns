# Last updated: 10/15/2025, 3:03:07 AM
class Solution(object):
    def uniqueOccurrences(self, arr):
        vals = {}  # Dictionary to store occurrences of each element
        count = {}  # Dictionary to store the count of occurrences

        # Count occurrences of each element in arr
        for n in arr:
            vals[n] = vals.get(n, 0) + 1

        # Now vals contains the occurrences of each element
        # We only need to check if these occurrences are unique
        occurrences = list(vals.values())

        # Check if all occurrences are unique
        if len(occurrences) == len(set(occurrences)):
            return True
        else:
            return False

# Last updated: 10/15/2025, 3:02:56 AM
class Solution(object):
    def largestAltitude(self, gain):
        altnow = 0
        apex = 0
        for i in range(len(gain)):
            altnow += gain[i]
            if altnow > apex:
                apex = altnow
        return apex
        
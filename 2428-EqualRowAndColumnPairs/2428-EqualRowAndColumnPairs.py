# Last updated: 10/15/2025, 3:02:52 AM
class Solution(object):
    def equalPairs(self, grid):        
        rows = {}
        for x in grid:
            #counts occurences since it'll add one only if 
            #the key is repeated in list grid
            rows[tuple(x)] = rows.get((tuple(x)),0) + 1 
            
        pairs = 0
        for c in range(len(grid)):
            c_tup = tuple(grid[r][c] for r in range(len(grid)))
            if c_tup in rows: pairs += rows[c_tup] 
    
        return pairs
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
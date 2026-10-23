class Solution:
    def isValid(self, s: str) -> bool:
        # case if there is only 1 
        if len(s) == 1:
            return False

        check = ""
        for br in s:
            check += br
            if check[-2:] == "()" or check[-2:] == "[]" or check[-2:] == "{}":
                check = check[:-2]
        
        if len(check) == 0:
            return True
        
        return False

        
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = 0

        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char,"",1)
            else:
                c = c+1

        if(c>0): 
            return False
        else:
            return True
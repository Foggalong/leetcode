class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Takes two strings (ransomNote, magazine) as input and then
        returns True if the first can be constructed from the letters
        of the second without replacement, or False otherwise.
        """

        # create a letter count dictionary
        magazine_dict = {chr(i): 0 for i in range(97,123)}
        for letter in magazine:
            magazine_dict[letter] +=1
        
        # work through ransomNote taking letters from magazine
        for letter in ransomNote:
            if magazine_dict[letter] > 0:
                magazine_dict[letter] -= 1
            else:
                return False

        return True


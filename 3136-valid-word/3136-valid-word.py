class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False
        
        for c in word:
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif c.isdigit():
                continue
            else:
                return False
        
        return has_vowel and has_consonant

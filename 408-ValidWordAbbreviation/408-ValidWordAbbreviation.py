class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isalpha():
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
            else: # decimal
                num = 0
                if int(abbr[i]) == 0: 
                    return False
                while i < len(abbr) and abbr[i].isdigit():
                    num = num * 10 + int(abbr[i])
                    i += 1
                j += num
        return j == len(word) and i == len(abbr)

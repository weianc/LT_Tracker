class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        left = right = 0
        wordDict = {}
        duplicateChars = 0
        
        while right < len(s):
            # expand window
            c = s[right]
            right += 1
            wordDict[c] = wordDict.get(c, 0) + 1
            if wordDict[c] > 1:
                duplicateChars += 1
            
            # shrink left bound
            while duplicateChars > 0:
                d = s[left]
                wordDict[d] -= 1
                if wordDict[d] == 1: 
                    duplicateChars -= 1
                left += 1
            
            maxlen = max(maxlen, right - left)
        
        return maxlen    
                

                


        
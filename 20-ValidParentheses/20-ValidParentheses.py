class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            else:
                if len(stk) == 0: 
                    return False
                else:
                    cur = stk.pop()
                    if cur == '(' and c != ')' or cur == '[' and c != ']' or cur == '{' and c != '}':
                        return False
        
        return len(stk) == 0

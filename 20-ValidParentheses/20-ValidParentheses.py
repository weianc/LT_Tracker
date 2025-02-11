class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            else:
                if not stk: 
                    return False
                else:
                    cur = stk.pop()
                    if cur == '(' and c != ')' or cur == '[' and c != ']' or cur == '{' and c != '}':
                        return False
        
        return not stk

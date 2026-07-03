class Solution:
    def isValid(self, s: str) -> bool:
        chars = []
        for c in s:
            if c in ['(','[','{'] :
                chars.append(c)
            elif c == ")" and len(chars)!=0 and chars[-1] != "(":
                return False
            elif c == "]" and len(chars)!=0 and chars[-1] != "[":
                return False
            elif c == "}" and len(chars)!=0 and chars[-1] != "{":
                return False
            elif len(chars)!=0:
                chars.pop()
            else:
                return False
        return True if len(chars) == 0 else False

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close={
            "}":"{",
            "]":"[",
            ")":"("
        }
        for i in s:
            if i not in close:
                
                stack.append(i)
            else:
                if not stack:
                    return False
                x=stack.pop()
                if close[i]!=x:
                    return False
        if not stack:
            return True
        else:
            return False
        
        
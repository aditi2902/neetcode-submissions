class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        for j in path.split('/'):
            if j =="..":
                if stack:
                    stack.pop()
                else:
                    continue
            elif j=="" or j==".":
                continue

            else:
                stack.append(j)
        
        return "/"+"/".join(stack)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=strs[0]
        for x in strs[1:]:
            if x.startswith(common):
                continue
            else:
                while common!="" and x.startswith(common)==False:
                    common=common[:-1]
        if len(strs)==2:
            if strs[1]!=common:
                return ""
        return common
        
        
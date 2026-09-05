
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts=defaultdict(list)
        for x in strs:
            temp=x
            x="".join(sorted(x))
            if dicts[x]:
                dicts[x].append(temp)
                continue
            dicts[x].append(temp)
        res=[]
        for x in dicts.keys():
            res.append(dicts[x])
        return res


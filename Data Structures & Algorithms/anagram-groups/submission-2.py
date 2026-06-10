
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict(list)
        result=[]
        for s in strs:
            key=tuple(sorted(s))
            map[key].append(s)
        for x in map.values():
            result.append(x)
        return result

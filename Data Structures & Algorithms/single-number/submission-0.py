class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=defaultdict(int)
        for x in nums:
            res[x]+=1
        for x in nums:
            if res[x]==1:
                return x
        return 0
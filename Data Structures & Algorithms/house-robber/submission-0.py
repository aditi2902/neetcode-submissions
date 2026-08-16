class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0
        for n in nums:
            temp=max(rob1+n,rob2) # alternate the +n for both ways 
            rob1=rob2
            rob2=temp
        return rob2 #LAST VALUE HAS FINAL SUM 
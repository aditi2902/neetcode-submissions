class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        ans=-1
        count=defaultdict(int)
        for i in nums:
            count[i]+=1
        for i in nums:
            if count[i]>(n//2):
                ans=i
        return ans


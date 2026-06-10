class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax=nums[0]
        curMin=nums[0]
        result=nums[0]

        for n in nums[1:]:
            temp=curMax
            curMax=max(n,curMax*n,curMin*n)
            curMin=min(n,temp*n,curMin*n)

            result=max(result,curMax)
        return result
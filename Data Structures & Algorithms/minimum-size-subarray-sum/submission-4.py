class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        minval=float('inf')
        sum_val=0
        l=0
        for r in range(n):
            sum_val+=nums[r]
            while sum_val >= target:
                minval=min(minval, r - l + 1)
                sum_val -= nums[l]
                l += 1
        
        return minval if minval != float('inf') else 0
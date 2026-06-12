class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        expected=1
        for x in nums:
            if x<expected:
                continue
            if x==expected:
                expected+=1
            if x>expected:
                return expected
        return expected
        
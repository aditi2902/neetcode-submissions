class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        for x in s:
            if x-1 not in s:
                length=1
                current=x
                while current+1 in s:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
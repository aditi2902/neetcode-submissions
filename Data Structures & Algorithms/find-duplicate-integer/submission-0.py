class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        #hashmap approach
        s=set()
        for x in nums:
            if x in s:
                return x
            s.add(x)
        return -1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        freq=defaultdict(int)
        for x in nums:
            freq[x]+=1
        k=0
        for x in freq:
            nums[k]=x
            k+=1
            
        return k
        

        
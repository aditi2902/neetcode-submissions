class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        k=0
        for j in range(n):
            if nums[j]!=val:
                nums[k]=nums[j]
                k+=1
        return k
        
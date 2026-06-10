class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        k=0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                k=i
                break
        nums.sort()
        flag=0
        for j in range(0,len(nums)):
            if nums[j]==target:
                flag=1
                break
        if flag==1:
            return (k+j)%len(nums)
        else:
            return -1
         
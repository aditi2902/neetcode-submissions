class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)-1
        if target>nums[h]:
            return h+1
        elif target<nums[l]:
            return 0
        while l<=h:
            mid=(l+h)//2
            if nums[mid]>target:
                h=mid-1
            elif nums[mid]<target:
                l=mid+1
            elif nums[mid]==target:
                return mid
           
        return l
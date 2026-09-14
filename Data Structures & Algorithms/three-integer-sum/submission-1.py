class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum=0
        res=[]
        for i in range(0,len(nums)):
            start=i+1
            end=len(nums)-1
            while start<end:
                sum=nums[i]+nums[start]+nums[end]
                if sum==0:
                    if [nums[i],nums[start],nums[end]] not in res:
                        res.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                        
                elif sum>0:
                    end-=1
                else :
                    start+=1
        return res
                
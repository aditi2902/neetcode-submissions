class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def func(index,subset):
            if index>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[index])
            func(index+1,subset)
            subset.pop()
            func(index+1,subset)
        func(0,[])
        return res
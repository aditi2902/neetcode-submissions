class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        def seq(index,subset):
            if index>=len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[index])
            seq(index+1,subset)
            subset.pop()
            seq(index+1,subset)

        seq(0,[])
        sum=0
        for x in res:
            temp=0
            for j in x:
                temp^=j
            sum+=temp
        return sum
        
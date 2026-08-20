class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def fun(index,subset):
            if len(subset)==k:
                res.append(subset.copy())
                return
            for i in range(index,n+1):
                subset.append(i) # add to current combination
                fun(i+1,subset) # always on the right side (greater values)
                subset.pop()
        fun(1,[])   # values between 1-n so 1
        return res          
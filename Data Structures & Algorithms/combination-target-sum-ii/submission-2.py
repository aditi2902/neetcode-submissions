class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def func(index,subset):
            total=sum(subset)
            if total==target:
                if subset not in res:
                    res.append(subset.copy())
                return
            if index>=len(candidates) or total>target:
                return
            subset.append(candidates[index])
            func(index+1,subset)
            subset.pop()
            next_i=index+1
            while next_i<len(candidates) and candidates[index]==candidates[next_i]:
                next_i+=1
            func(next_i,subset)
        func(0,[])
        return res

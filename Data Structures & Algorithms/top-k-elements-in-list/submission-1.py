class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=defaultdict(int)
        n=[]
        for i in nums:
            result[i]+=1
        z=0
        for j in range(0,k):
            mk=max(result,key=result.get)
            n.append(mk)
            del result[mk]
        return n
            
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = 0
        arr=[]
        n=len(nums)
        freq=defaultdict(int)
        for x in nums:
            freq[x]+=1
        for j in freq:
            if freq[j]>(n//3):
                arr.append(j)
        return arr
        
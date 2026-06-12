class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq=defaultdict(int)
        freq[0]=1
        currsum=0
        count=0
        for n in nums:
            currsum+=n
            count+=freq[currsum-k]
            freq[currsum]+=1
        return count
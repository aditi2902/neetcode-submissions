class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p=-1
        total=0
        temp=0
        for i in range(0,len(prices)):
            max_p=0
            for j in range(i+1,len(prices)):
                max_p=max(max_p,prices[j])
                if max_p>=prices[i]:
                    temp= max_p - prices[i]
                if temp>total:
                    total=temp
        return total
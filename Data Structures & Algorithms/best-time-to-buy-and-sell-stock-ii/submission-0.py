class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dif=[0]*n
        total=0
        for i in range(0,n-1):
            dif[i]=prices[i+1]-prices[i]
        for x in dif:
            if x>0:
                total+=x
        return total



        
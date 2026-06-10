class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=9999
        n=len(prices)
        rightMax=[0]*n
        rightMax[n-1]=prices[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],prices[i])
        maxn=-999
        for i in range(0,n):
            if rightMax[i]-prices[i]>maxn:
                maxn=rightMax[i]-prices[i]
        return maxn

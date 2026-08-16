class Solution:
    def climbStairs(self, n: int) -> int:
        ##bottom up approach - always to last step you take 1 say n=5 0 is the ground
        ##5 to 4 is 1 4+2 would give six 
        ##like fibonacci 
        one,two=1,1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp
        return one
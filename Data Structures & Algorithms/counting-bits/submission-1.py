class Solution:
    def countBits(self, n: int) -> List[int]:
       
        res=[0]*(n+1)
        for x in range(n+1):
            temp=x
            count=0
            while x>0:
                r=x%2
                if r==1:
                    count+=1
                x=x//2
            res[temp]=count
        return res
##
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(n + 1):
            one = 0
            for i in range(32):
                if num & (1 << i):
                    one += 1
            res.append(one)
        return res

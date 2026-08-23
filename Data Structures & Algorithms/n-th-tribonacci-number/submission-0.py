class Solution:
    def tribonacci(self, n: int) -> int:
        first,second,third=0,1,1
        if n==0:
            return 0
        if n>=2:
            for i in range(1,n):
                temp=first+third+second
                first=second
                second=third
                third=temp
        return second

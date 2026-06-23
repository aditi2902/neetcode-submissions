class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=len(a)-1
        y=len(b)-1
        carry=0
        res=[]
        while x>=0 or y>=0 or carry:
            digA=int(a[x]) if x>=0 else 0
            digB=int(b[y]) if y>=0 else 0
            ttl=digA+digB+carry
            res.append(str(ttl%2))
            carry=ttl//2
            x-=1
            y-=1
        return "".join(res[::-1])


        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t1=sorted(t)
        if len(t1)!=len(s1) :
            return False
        for i in range(0,len(s1)):
            if s1[i]==t1[i]:
                continue
            else:
                return False
           
               
       
           
        return True

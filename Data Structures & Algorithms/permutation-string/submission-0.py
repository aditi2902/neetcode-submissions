class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        end=n1-1
        start=0
        ## counter makes dictionary of freq of all values in string
        freq=Counter(s1)

        while start <= n2 - n1:
            window_freq = Counter(s2[start:start+n1])
            if freq == window_freq:
                return True
            start+=1
        return False

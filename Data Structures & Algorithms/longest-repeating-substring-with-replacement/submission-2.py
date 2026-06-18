class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## keep the character appearing most -> MAX FREQ
        ## no. of replacements -> window_size-max_freq
        n=len(s)
        l=0
        count=0
        fm=defaultdict(int)
        maxFreq=0
        for r in range(n):
            fm[s[r]]+=1
            maxFreq=max(maxFreq,fm[s[r]])
            while (r-l+1)-maxFreq>k:
                fm[s[l]]-=1
                l+=1
            count=max(count,r-l+1)
        return count
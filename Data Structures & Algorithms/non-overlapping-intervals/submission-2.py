class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        ## when 2 overlap remove the interval ending last
        ## x1 x2 y1 y2  : x2 > y1 overlap
        ##  x1 x2 y1 y2 : x2 <= y1
        ## cant delete within list as for i 0->n the n keeps reducing => index out of bound
        ## NEED TO SORT
        count = 0
        n=len(intervals)
        intervals.sort()
        if n==0:
            return 0
        prev_end = intervals[0][1]
        for x in range(1,n):
            if intervals[x][0]<prev_end:
                count+=1
                if intervals[x][1]<prev_end:
                    prev_end=intervals[x][1]
            else:
                prev_end=intervals[x][1]  
            
        return count


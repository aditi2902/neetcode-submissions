class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar=-1
        start=0
        end=len(heights)-1
        while start<end:
            height=min(heights[start],heights[end])
            width=end-start
            area=height*width
            if area>maxar:
                maxar=area
            if heights[start]>heights[end]:
                end-=1
            else:
                start+=1
        return maxar

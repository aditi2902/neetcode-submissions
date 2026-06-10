class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar=0
        left =0
        right =len(heights)-1
        while left<right and right<len(heights):
            ar=(right-left)*min(heights[left],heights[right])
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1

            if ar>maxar:
                maxar=ar
        return maxar
            
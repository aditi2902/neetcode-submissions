class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=m+n
        k=0
        for i in range(x-1,-1,-1):
            if nums1[i]!=0:
                break
            if nums1[i]==0:
                nums1[i]=nums2[k]
                k+=1
            
        nums1.sort()
        
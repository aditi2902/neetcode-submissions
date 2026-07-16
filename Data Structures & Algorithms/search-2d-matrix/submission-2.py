class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,h=0,len(matrix[0])*len(matrix)-1
        while l<=h:
            mid=(l+h)//2
            row_m=mid//len(matrix[0])
            col_m=mid%len(matrix[0]) #both row_m and col_m usenumber of cols
            if matrix[row_m][col_m]==target:
                return True
            elif matrix[row_m][col_m]>target:
                h=mid-1
            else:
                l=mid+1
        return False



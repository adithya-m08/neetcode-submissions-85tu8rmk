class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        l,r=0,rows-1
        row=-1

        while l<=r:
            m=(l+r)//2
            if target>matrix[m][-1]:
                l=m+1
            elif target<matrix[m][0]:
                r=m-1
            else:
                row=m
                break

        if row==-1:
            return False
        
        l,r=0, cols-1

        while l<=r:
            m=(l+r)//2
            if target>matrix[row][m]:
                l=m+1
            elif target<matrix[row][m]:
                r=m-1
            else:
                return True
        
        return False

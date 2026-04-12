class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=0,len(matrix)-1

        while i<=j:
            m=(i+j)//2
            if(matrix[m][-1]<target):
                i=m+1
            elif(matrix[m][0]>target):
                j=m-1
            else:
                break
        row=m
        i,j=0,len(matrix[0])-1
        while i<=j:
            m=(i+j)//2
            if(matrix[row][m]<target):
                i=m+1
            elif(matrix[row][m]>target):
                j=m-1
            else:
                return True
        return False
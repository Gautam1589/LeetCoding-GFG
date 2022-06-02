class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_=0
        n=len(mat)
        for i in range(n):
            for j in range(n):
                if i==j:
                    sum_+=mat[i][j]
                elif i==n-j-1:
                    sum_+=mat[i][j]
        return sum_
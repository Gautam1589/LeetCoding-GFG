class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.__mat=matrix
        self.__dp=self.pre_calculation(matrix)
        
    def pre_calculation(self,matrix):
        dp=[[0]*(len(matrix[0])+1) for i in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])+1):
                dp[i][j]=dp[i][j-1]+matrix[i][j-1]
        
        return dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_=0
        for i in range(row1,row2+1):
            sum_+=self.__dp[i][col2+1]-self.__dp[i][col1]
        
        return sum_
    
    #brute force
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sum_=0
    #     for i in range(row1,row2+1):
    #         for j in range(col1,col2+1):
    #             sum_+=self.__mat[i][j]
    #     return sum_


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
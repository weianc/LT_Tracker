class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix) + 1
        col = len(matrix[0]) + 1
        self.preSum = [[0] * col for _ in range(row)]

        # construct preSum matrix according to matrix 
        for r in range(1, row):
            for c in range(1, col):
                self.preSum[r][c] = self.preSum[r-1][c] + self.preSum[r][c-1] + matrix[r-1][c-1] - self.preSum[r-1][c-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] - self.preSum[row1][col2+1] - self.preSum[row2+1][col1] + self.preSum[row1][col1]
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
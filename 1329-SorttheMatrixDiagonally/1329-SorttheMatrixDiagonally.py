class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0] * n] * m
        diagonal = {}
        # put element with key: r-c into map
        for r in range(m): 
            for c in range(n):
                key = r - c
                if key not in diagonal:
                    diagonal[key] = []
                diagonal[key].append(mat[r][c])

        # sort each diagnal 
        for key in diagonal: 
            diagonal[key].sort()
        
        # put back to res 
        for r in range(m): 
            for c in range(n):
                key = r - c
                mat[r][c] = diagonal[key].pop(0)
        
        return mat
        

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        #for r in range(rows//2):
        top = 0
        bottom = rows-1
        while top < bottom:
            for c in range(cols):
                matrix[top][c], matrix[bottom][c] = matrix[bottom][c], matrix[top][c]
            top+=1
            bottom-=1

        for r in range(rows):
            for c in range(r+1, cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


                
            
            
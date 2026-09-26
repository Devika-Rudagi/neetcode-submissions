class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        lst = []
        t,b,l,r = 0,rows,0,cols
        
        while t<b and l<r:
            for i in range(l,r):
                lst.append(matrix[t][i])
            t+=1

            for i in range(t, b):
                lst.append(matrix[i][r-1])
            r-=1
            if t<b:
                for i in range(r-1,l-1,-1):
                    lst.append(matrix[b-1][i])
                b-=1
            if l<r:
                for i in range(b-1, t-1, -1):
                    lst.append(matrix[i][l])
                l+=1

        
        return lst


        
        

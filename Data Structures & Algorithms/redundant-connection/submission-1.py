class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [0 for _ in range(len(edges)+1)]

        def find(i):
            while i!=par[i]:
                par[i] = par[par[i]]
                i = par[i]
            return par[i]
        
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return False
            
            if rank[rx] > rank[ry]:
                par[ry] = rx
                rank[rx]+=1
            else:
                par[rx] = ry
                rank[ry]+=1
            return True

        for u, v in edges:
            if not union(u,v):
                return [u, v]
             
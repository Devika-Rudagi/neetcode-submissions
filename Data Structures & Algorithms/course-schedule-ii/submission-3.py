class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        res = []
        for u, v in prerequisites:
            ind[u] +=1
            adj[v].append(u)
        
        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in adj[cur]:
                ind[nei]-=1
                if ind[nei] == 0:
                    q.append(nei)
        
        if len(res)!= numCourses:
            return []
        return res


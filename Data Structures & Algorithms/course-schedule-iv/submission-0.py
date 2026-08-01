class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ind = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        res = []
        reachable = [set() for _ in range(numCourses)]

        for u, v in prerequisites:
            ind[v] +=1
            adj[u].append(v)

        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
        
        while q:
            cur = q.popleft()
            for nei in adj[cur]:
                reachable[nei].add(cur)
                reachable[nei] = reachable[cur].union(reachable[nei])
                ind[nei]-=1
                if ind[nei] == 0:
                    q.append(nei)
        
        return [u in reachable[v] for u, v in queries]
        # for u, v in queries:
        #     if u in reachable[v]:
        #         res.append(True)
        #     else:
        #         res.append(False)
        
        # return res


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(u):
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u
        
        parents = [i for i in range(n)]
        
        for u,v in edges:
            pu, pv = find(u), find(v)
            
            if pu == pv:
                return False
            
            parents[pv] = pu
        
        return len({find(i) for i in range(n)}) == 1
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        def build_adj(edges):
            adj = defaultdict(list)
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def DFS(u, parent, max_len, adj):
            if max_len < 0:
                return 0
            count = 1
            for v in adj[u]:
                if v != parent:
                    count += DFS(v, u, max_len - 1, adj)
            return count
        
        adj1 = build_adj(edges1)
        adj2 = build_adj(edges2)

        max_cnt2 = 0
        for i in range(m):
            max_cnt2 = max(max_cnt2, DFS(i, -1, k - 1, adj2))

        res = []
        
        for i in range(n):
            count = DFS(i, -1, k, adj1)
            res.append(count + max_cnt2)
        return res
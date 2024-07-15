class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        if self.par[v1] != v1:
            self.par[v1] = self.find(self.par[v1])
        return self.par[v1]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.par[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.par[root1] = root2
        else:
            self.par[root2] = root1
            self.rank[root1] += 1
        
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i, edge in enumerate(edges):
            edge.append(i)  # Append original index to edge
        
        edges.sort(key=lambda x: x[2])  # Sort edges by weight
        
        def calculate_mst_weight(exclude_edge=None):
            uf = UnionFind(n)
            mst_weight = 0
            if exclude_edge is not None and uf.union(exclude_edge[0], exclude_edge[1]):
                mst_weight += exclude_edge[2]
            
            for edge in edges:
                if edge == exclude_edge:
                    continue
                if uf.union(edge[0], edge[1]):
                    mst_weight += edge[2]
            
            return mst_weight
        
        mst_weight = calculate_mst_weight()
        critical, pseudo = [], []
        
        for edge in edges:
            if calculate_mst_weight(edge) > mst_weight:
                critical.append(edge[3])  # Append original index
            else:
                if calculate_mst_weight() == mst_weight:
                    pseudo.append(edge[3])  # Append original index
        
        return [critical, pseudo]
        
# # Exemplos de uso
# if __name__ == "__main__":
#     n1 = 5
#     n2 = 4
#     edges1 = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
#     edges2 = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
#     solution = Solution()
#     print(solution.findCriticalAndPseudoCriticalEdges(n1, edges1))
#     print(solution.findCriticalAndPseudoCriticalEdges(n2, edges2))
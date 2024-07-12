import heapq

class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        if n == 1:
            return 0

        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        min_heap = [(0, 0)]
        total_cost = 0
        in_mst = set()

        while len(in_mst) < n:
            cost, u = heapq.heappop(min_heap)
            if u in in_mst:
                continue
            in_mst.add(u)
            total_cost += cost

            for v in range(n):
                if v not in in_mst:
                    heapq.heappush(min_heap, (manhattan_distance(points[u], points[v]), v))

        return total_cost

# # Exemplos de uso
# if __name__ == "__main__":
#     points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
#     points2 = [[3,12],[-2,5],[-4,1]]
#     solution = Solution()
#     print(solution.minCostConnectPoints(points1))
#     print(solution.minCostConnectPoints(points2))
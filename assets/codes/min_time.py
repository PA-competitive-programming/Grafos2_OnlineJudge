class Solution(object):
    def minimumTime(self, n, edges, disappear):
        graph = [[] for _ in range(n)]
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        min_time = [float('inf')] * n
        min_time[0] = 0
        queue = [(0, 0)]
        
        while queue:
            current_time, u = queue.pop(0)
            
            if current_time >= disappear[u]:
                continue
            
            for v, length in graph[u]:
                new_time = current_time + length
                
                if new_time < min_time[v] and new_time < disappear[v]:
                    min_time[v] = new_time
                    queue.append((new_time, v))
                    queue.sort()

        answer = [t if t < float('inf') else -1 for t in min_time]
        return answer

# # Exemplos de uso
# if __name__ == "__main__":
#     solution = Solution()
    
#     n1 = 3
#     edges1 = [[0,1,2],[1,2,1],[0,2,4]]
#     disappear1 = [1,1,5]
#     print(solution.minimumTime(n1, edges1, disappear1))

#     n2 = 3
#     edges2 = [[0,1,2],[1,2,1],[0,2,4]]
#     disappear2 = [1,3,5]
#     print(solution.minimumTime(n2, edges2, disappear2))

#     n3 = 2
#     edges3 = [[0,1,1]]
#     disappear3 = [1,1]
#     print(solution.minimumTime(n3, edges3, disappear3))

#     n4 = 50000
#     edges4 = [[i, i+1, 1] for i in range(49999)]
#     disappear4 = [100000] * 49999 + [1]
#     print(solution.minimumTime(n4, edges4, disappear4))

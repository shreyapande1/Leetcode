class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def bfs(edges):
            if not edges:
                return 0
            
            n = len(edges) + 1
            graph = defaultdict(set)

            
            for i, j in edges:
                graph[i].add(j)
                graph[j].add(i)
                            
            leaves = []
            for i in range(n):
                if len(graph[i]) == 1:
                    leaves.append(i)
            
            remain = n
            step = 0
            while remain > 2:
                remain -= len(leaves)
                new_leaves = []
                for leaf in leaves:
                    neighbor = graph[leaf].pop()
                    graph[neighbor].discard(leaf)
      
                    if len(graph[neighbor]) == 1:
                        new_leaves.append(neighbor)
                step += 1
                leaves = new_leaves
            return step * 2 + 1 if remain == 2 else step * 2
        
        diameter1 = bfs(edges1)
        diameter2 = bfs(edges2)

        d1 = math.ceil(diameter1 / 2)
        d2 = math.ceil(diameter2 / 2)
        return max(d1 + d2 + 1, max(diameter1, diameter2))


        
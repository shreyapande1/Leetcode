class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        visited = [False] * n
        path_visited = [False] * n

        def dfs(node):
            # If already visited in current path, it's part of a cycle
            if path_visited[node]:
                return False
            
            # If already explored and known status
            if visited[node]:
                return safe[node]
            
            # Mark as visited in current path
            visited[node] = True
            path_visited[node] = True
            
            # Check all neighbors
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            # No cycles found, mark as safe
            path_visited[node] = False
            safe[node] = True
            return True
        
        # Run DFS on all nodes
        for i in range(n):
            dfs(i)
        
        # Collect safe nodes
        return [i for i in range(n) if safe[i]]
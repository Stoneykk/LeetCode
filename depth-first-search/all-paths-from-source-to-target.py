class Solution:
    def dfs(self, graph, node, target, path, result):
        if node == target:
            result.append(path[:])
            return
        for other in graph[node]:
            path.append(other)
            self.dfs(graph, other, target, path, result)
            path.pop()
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
       result = []
       start = 0
       target = len(graph) - 1
       self.dfs(graph, start, target, [start], result)
       return result
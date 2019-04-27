class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        INFINITY = float('inf')
        graph = {}
        for time in times:
            u, v, w = tuple(time)
            if not u in graph:
                graph[u] = {}
            graph[u][v] = w
        
        dist = [INFINITY] * (N + 1)
        vertexs = [x for x in range(0, N + 1)]
        dist[K] = 0
        
        while vertexs:
            u = min(vertexs, key=lambda x: dist[x])
            if dist[u] == INFINITY:
                break
            vertexs.remove(u)
            if u in graph:
                for (v, w) in graph[u].items():
                    alt = dist[u] + w
                    if alt < dist[v]:
                        dist[v] = alt
        if INFINITY in dist[1:]:
            return -1
        return max(dist[1:])
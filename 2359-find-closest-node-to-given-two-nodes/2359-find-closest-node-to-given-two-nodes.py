class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """

        def get_distances(start):
            n = len(edges)
            dist = [-1] * n
            visited = set()
            curr = start
            d = 0

            while curr != -1 and curr not in visited:
                dist[curr] = d
                visited.add(curr)
                d += 1
                curr = edges[curr]

            return dist

       
        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

       
        min_dist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i

        return result

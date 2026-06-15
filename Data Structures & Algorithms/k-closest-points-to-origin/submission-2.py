class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(res, (-distance, point))
            if len(res) > k:
                heapq.heappop(res)
        return [point for (_, point) in res]
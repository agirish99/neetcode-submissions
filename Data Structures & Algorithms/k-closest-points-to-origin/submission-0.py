import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x**2 + y**2

            heapq.heappush(heap, (-distance,point)) #Storing as a max heap

            if (len(heap) > k):
                heapq.heappop(heap)

        return [point for distance,point in heap]

        
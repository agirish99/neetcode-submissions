import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if( len(heap) > k): #Keep heap as size of k
                heapq.heappop(heap)

        return heap[0]
        
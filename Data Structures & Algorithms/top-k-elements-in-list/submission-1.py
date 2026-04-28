class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_N = {}

        for num in nums:
            count_N[num] = count_N.get(num, 0) + 1

        heap = []

        for num, frq in count_N.items():
            heapq.heappush(heap, (frq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for frq, num in heap]
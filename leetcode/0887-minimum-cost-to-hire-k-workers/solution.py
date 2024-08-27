class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        min_cost = float('inf')  # running minimum cost found
        sum_qual = 0             # running sum of worker quality

        # heap workers descending using negative quality
        heap = []

        # iterate through workers in ascending order of quality:wage ratio
        for q, w in sorted(zip(quality, wage), key=lambda x: x[1]/x[0]):
            # add worker to the stack
            sum_qual += q
            heappush(heap, -q)
            # if too many, remove worst and subtract quality from total
            if len(heap) > k: sum_qual += heappop(heap)
            # if exactly k workers, update the running minimum cost
            if len(heap) == k: min_cost = min(min_cost, sum_qual*w/q)

        return min_cost

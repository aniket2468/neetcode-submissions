class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert all the weights to negatives to simulate max-heap
        stones = [-s for s in stones]
        heapq.heapify(stones) #O(n)

        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            #if they are not equal, push back the difference
            if first != second:
                new_weight = -(first - second)
                heapq.heappush(stones, new_weight)
        
        return -stones[0] if stones else 0

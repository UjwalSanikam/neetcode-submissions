class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            total = 0
            for i in range(len(piles)):
                total = total + math.ceil(piles[i] / mid)
            if total > h:
                left = mid + 1
            elif total <= h:
                result = mid
                right = mid - 1
        return result
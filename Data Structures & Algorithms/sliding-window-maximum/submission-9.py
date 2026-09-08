class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        result = []
        q = deque()  # Stores indices of elements
    
        for i, num in enumerate(nums):
        # 1. Remove indices that are out of the current window's range
            if q and q[0] < i - k + 1:
                q.popleft()
        
        # 2. Remove elements smaller than the current element from the back
            while q and nums[q[-1]] < num:
                q.pop()
            
        # Add the current element's index
            q.append(i)
        
        # 3. Once the first window is fully formed, append max to result
            if i >= k - 1:
                result.append(nums[q[0]])
            
        return result
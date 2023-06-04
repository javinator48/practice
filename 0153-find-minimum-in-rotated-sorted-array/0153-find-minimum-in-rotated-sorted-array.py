class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')
        high = len(nums) - 1 
        low = 0 
        
        while high > low: 
            mid = (high + low) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] < nums[high]: 
                high = mid -1 
            else: 
                low = mid + 1 
        return min(minimum, nums[low])
            
            
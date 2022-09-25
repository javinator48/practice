class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use double pointer 
        left = 0 
        right = len(nums)-1 
        minimum = float('inf')
        # one element
        if len(nums) == 1: 
            return nums[0]
        # no rotation
        if nums[right] > nums[left]: 
            return nums[left]
        
        while left <= right:
            mid = left + (right - left)//2
            #if the mid element is greater tha its next element 
            if nums[mid] > nums[mid+1]: 
                return nums[mid+1]
            # if the mid element is lesser than its previous element
            if nums[mid] < nums[mid-1]: 
                return nums[mid]
            # if the mid element value is greater than the 0th element 
            if nums[mid] > nums[0]: 
                left = mid + 1 
                
            # if nums[0] is greater than the mid value 
            else: 
                right = mid -1 
                
            
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashmap = {}
       #two pointers 
        l = 1 
        for  r in range(len(nums)-1): 
            if nums[r] != nums[r+1]: 
                nums[l] = nums[r+1]
                l += 1
        return l
        
        
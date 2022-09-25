class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique = set(list(range(0,len(nums)+1)))
        for integer in nums: 
            if integer in unique: 
                unique.remove(integer)
        
        return unique.pop()
                
        
        
        
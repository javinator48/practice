class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        for j in range(len(nums)): 
            if target - nums[j] in hashtable and hashtable.get(target-nums[j], None)!= j: 
                return [j, hashtable[target - nums[j]]]
    
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left_index in range(len(nums)):
            for right_index in range(left_index+1 , len(nums)): 
                if nums[left_index] + nums[right_index] == target: 
                    return [left_index, right_index]
        
class Solution:
    #Bruth Force 
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for left_index in range(len(nums)):
    #         for right_index in range(left_index+1 , len(nums)): 
    #             if nums[left_index] + nums[right_index] == target: 
    #                 return [left_index, right_index]
    #Alt solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {} 
        for i in range(len(nums)): 
            hashtable[nums[i]] = i 
        for i in range(len(nums)): 
            complement = target -nums[i]
            if complement in hashtable and hashtable[complement]!= i: 
                return[i, hashtable[complement]]
class Solution:
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else: 
            firstnums = nums[0:len(nums)-1]
            secondnums = nums[1:len(nums)]

        
        def robBasic(nums: List[int]) -> int:

            if len(nums) == 1: 
                return nums[0]
            maxRobbedAmount = [None for _ in range(len(nums)+1)]
            N = len(nums)
            maxRobbedAmount[0], maxRobbedAmount[1] = 0, nums[0]
            if N >= 2: 
        
                for i in range(2, N+1): 
                    maxRobbedAmount[i] = max(maxRobbedAmount[i-2] + nums[i-1], maxRobbedAmount[i-1])
                    print(i)
                    print("executed")
            return maxRobbedAmount[N]
        return max(robBasic(firstnums), robBasic(secondnums))
        
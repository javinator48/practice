class Solution:
    def rob(self, nums: List[int]) -> int:
        #empty case 
        if not nums: 
            return 0 
        maxRobbedAmount = [None for _ in range(len(nums)+1)]
        N = len(nums)
        maxRobbedAmount[0], maxRobbedAmount[1] = 0, nums[0]
        for i in range(2, N+1): 
            maxRobbedAmount[i] = max(maxRobbedAmount[i-2] + nums[i-1], maxRobbedAmount[i-1])
      
        return maxRobbedAmount[N]
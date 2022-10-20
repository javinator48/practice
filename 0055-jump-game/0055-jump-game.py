class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ##my solution
#         #element in array represents if you can jump to the last index 
#         dp = ["unknown"]*len(nums)
#         #last position can jump to itself
#         dp[-1] = "yes"
#         for index in reversed(range(len(nums)-1)): 
#             #print()
#             #print(index)
#             for additionalIndex in range(1,nums[index]+1):
#                 if index+additionalIndex >= len(dp): 
#                     break
#                 if dp[index+additionalIndex] == "yes":
#                     dp[index] = "yes"
#                     break 
#             if dp[index] == "unknown": 
#                 dp[index] = "no"
                
#         output = (dp[0] == "yes")
#         return output
        #Other's solution 
        dp = [False]*len(nums)
        dp[0] = True
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if dp[j] == True and nums[j] + j >= i:
                    dp[i] = True
                    break
        return dp[-1]
            
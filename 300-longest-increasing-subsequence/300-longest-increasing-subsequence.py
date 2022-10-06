class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #populate a list with length len(nums)
        dp = []
        for element in nums: 
            dp.append(0)
        for index in range(0, len(nums)):
            #Iterate through previous storage to get info
            #answer = []
            
            
            maxLen = 1 
               
            for previousElementIndex in range(0,index):
                
                #if we can create a bigger substring from prevbious substrings 
                
                if nums[index] > nums[previousElementIndex] and dp[previousElementIndex]+1 > maxLen: 
                    maxLen = dp[previousElementIndex] + 1 
            dp[index] = maxLen
        return max(dp)
                    
                    
                
                
                    
                    
                
                    
                
            
                
            
            
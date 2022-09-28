class Solution:
    def climbStairs(self, n: int) -> int:
        #basecases
        if n == 1: 
            return 1
        
        dp = [0 for i in range(n+1)] 
        dp[0] = 1 
        dp[1] = 2 
        for aint in range(2, n): 
            dp[aint] = dp[aint-1] + dp[aint-2]
        return dp[n-1]
        
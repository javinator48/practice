class Solution:
    def numDecodings(self, s: str) -> int:
        #each element at an index represent number of ways to decode a word with length index 
        dp = defaultdict(int)
        
        if s[0] == '0':
            return 0
         
        
        is_valid = lambda x: x != '' and 1 <= int(x) <= 26 and x[0] != '0'
        dp[0] = 1 
        for i in range(1,len(s)+1): 
            dp[i] += dp[i-1] if is_valid(s[i-1]) else 0 
            
            dp[i] += dp[i-2] if is_valid(s[i-2:i]) else 0 
        return dp[len(s)]
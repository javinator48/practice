class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)
        dp[-1] = 1
        is_valid = lambda x: x != '' and 1 <= int(x) <= 26 and x[0] != '0'
        for i in range(len(s)):
            dp[i] += dp[i-1] if is_valid(s[i]) else 0 
            dp[i] += dp[i-2] if is_valid(s[i-1:i+1]) else 0 
        return dp[len(s)-1]
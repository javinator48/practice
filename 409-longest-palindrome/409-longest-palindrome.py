class Solution:
    def longestPalindrome(self, s):
        odds = sum([freq % 2 for _,freq in Counter(s).items()])
        return len(s) if odds == 0 else len(s) - odds + 1 
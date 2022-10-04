# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #two pointers 
        left = 1
        right = n 
        if n == 1 and isBadVersion(n): 
            return n 
        
        
        while left <= right: 
            mid = ((right - left)//2) + left 
            if isBadVersion(mid): 
                right = mid -1
                if not isBadVersion(mid-1): 
                    return mid 
            else: 
                left = mid + 1 
        return mid 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        totalsum = []
        asum = 0 
        for num in nums: 
            asum += num
            totalsum.append(asum)
        return totalsum
        
        
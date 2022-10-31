class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals = sorted(intervals, key=lambda x:x[0])
        intervals.sort()
        print(intervals)
        res = intervals[0]
    
        counter = 0 
        for i in range(1,len(intervals)): 
            if intervals[i][0] < res[1]:
                counter += 1
                if res[1] > intervals[i][1]:
                    res = intervals[i]
            else: 
                res = intervals[i]
        return counter
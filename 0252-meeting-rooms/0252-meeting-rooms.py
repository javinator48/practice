class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        output = []
        for i in range(len(intervals)): 
            
            if not output or intervals[i][0] >= output[-1][1]: 
                output.append(intervals[i])
            else: return False
        return True 
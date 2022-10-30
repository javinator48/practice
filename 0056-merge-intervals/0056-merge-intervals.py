class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(len(intervals)): 
                
            if not output or intervals[i][0] > output[-1][1]:
                output.append(intervals[i])
            else:
                newinterval = [min(output[-1][0], intervals[i][0]), max(output[-1][1], intervals[i][1])]
                output[-1] = newinterval
        return output
                